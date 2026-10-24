"""Reproduce the financial sample analysis. Python 3.10+, pandas and openpyxl."""
from pathlib import Path
import hashlib
import json
import sqlite3
import urllib.request
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
URL='https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx'

def main():
    path=ROOT/'data/Financial-Sample.xlsx'
    path.parent.mkdir(parents=True,exist_ok=True)
    if not path.exists():urllib.request.urlretrieve(URL,path)
    df=pd.read_excel(path,keep_default_na=False)
    df.columns=df.columns.str.strip()
    for c in ['Segment','Country','Product','Discount Band']:df[c]=df[c].str.strip()
    numeric=['Units Sold','Manufacturing Price','Sale Price','Gross Sales','Discounts','Sales','COGS','Profit']
    for c in numeric:df[c]=pd.to_numeric(df[c],errors='raise')
    df['Date']=pd.to_datetime(df['Date'],errors='raise')
    assert len(df)==700
    assert not df.isna().any().any()
    assert (abs(df['Gross Sales']-df['Discounts']-df['Sales'])<1e-6).all()
    assert (abs(df['Sales']-df['COGS']-df['Profit'])<1e-6).all()
    assert (abs(df['Units Sold']*df['Sale Price']-df['Gross Sales'])<1e-6).all()
    assert (df['Date'].dt.year==df['Year']).all()
    assert (df['Date'].dt.month==df['Month Number']).all()
    out=ROOT/'reports'
    out.mkdir(exist_ok=True)
    with sqlite3.connect(':memory:') as db:
        df.to_sql('financials',db,index=False)
        sql=db.execute('SELECT SUM(Sales),SUM(Profit),SUM(Discounts) FROM financials').fetchone()
        assert all(abs(a-b)<1e-5 for a,b in zip(sql,[df['Sales'].sum(),df['Profit'].sum(),df['Discounts'].sum()]))
    summary={c:float(df[c].sum()) for c in numeric if c not in ['Manufacturing Price','Sale Price']}
    summary['Profit Margin']=summary['Profit']/summary['Sales']
    summary['Discount Rate']=summary['Discounts']/summary['Gross Sales']
    summary['Rows']=len(df)
    summary['Period']=[df['Date'].min().date().isoformat(),df['Date'].max().date().isoformat()]
    summary['Source SHA256']=hashlib.sha256(path.read_bytes()).hexdigest()
    result={'summary':summary,'groups':{}}
    for dimension in ['Segment','Country','Product','Discount Band','Year']:
        g=df.groupby(dimension,dropna=False)[['Sales','Profit','Discounts','Gross Sales','Units Sold']].sum()
        g['Profit Margin']=g['Profit']/g['Sales']
        g['Discount Rate']=g['Discounts']/g['Gross Sales']
        g.to_csv(out/(dimension.lower().replace(' ','_')+'_summary.csv'))
        result['groups'][dimension]=g.reset_index().to_dict(orient='records')
    # 2013 only has Sep-Dec. Compare matching months rather than incomplete annual totals.
    comparable=df[df['Date'].dt.month>=9].groupby('Year')[['Sales','Profit']].sum()
    result['comparable_sep_dec']=comparable.reset_index().to_dict(orient='records')
    df.to_csv(ROOT/'data/financials_clean.csv',index=False,date_format='%Y-%m-%d')
    (out/'analysis.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
