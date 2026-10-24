# Financial performance review

Portfolio case study using Microsoft's Financial Sample. This is sample business data, not an analysis commissioned by the represented company.

## Management takeaway

Enterprise generates substantial sales while losing money. Review its pricing, discount approval and cost assumptions before pursuing additional volume. Government contributes most total profit. Country and product rankings differ between revenue and margin, so a sales-only dashboard would conceal important trade-offs.

## Baseline

The 700-row sample covers September 2013–December 2014, five countries, five market segments and six products. Rows are source sales records, not identified customer transactions. Amounts retain the workbook's monetary convention; no currency conversion is applied.

| KPI | Result | Definition |
| --- | ---: | --- |
| Gross sales | 127,931,598.50 | Sum of Gross Sales |
| Discounts | 9,205,248.24 | Sum of Discounts |
| Net sales | 118,726,350.26 | Gross sales less discounts |
| Cost of goods sold | 101,832,648.00 | Sum of COGS |
| Profit | 16,893,702.26 | Net sales less COGS |
| Profit margin | 14.23% | Total profit / total net sales |
| Discount rate | 7.20% | Total discounts / total gross sales |
| Units sold | 1,125,806 | Sum of Units Sold, preserving fractional source quantities |

## Segment performance

| Segment | Net sales | Profit | Profit margin |
| --- | ---: | ---: | ---: |
| Government | 52,504,260.67 | 11,388,173.17 | 21.69% |
| Small Business | 42,427,918.50 | 4,143,168.50 | 9.77% |
| Enterprise | 19,611,694.38 | -614,545.63 | -3.13% |
| Midmarket | 2,381,883.08 | 660,103.08 | 27.71% |
| Channel Partners | 1,800,593.64 | 1,316,803.14 | 73.13% |

Channel Partners has the strongest margin but a much smaller sales base. Its margin alone does not establish scalable demand or an achievable growth opportunity. Enterprise's negative contribution warrants a product/country/discount drill-down.

## Products, countries and discounts

- Paseo leads net sales (33.01 million) and profit (4.80 million). Amarilla has the highest product margin, 15.86%.
- The United States leads country net sales (25.03 million) but has the lowest country margin, 11.97%. Germany has the highest country margin, 15.66%, while France leads total country profit at 3.78 million.
- High-discount records have a 9.07% margin, compared with 21.86% for no-discount records. Product, segment and country mix can explain part of this difference. The comparison does not prove the effect of changing discounts.

## Comparable-period growth

2013 contains only September–December. A full-year 2014 versus partial-year 2013 comparison overstates comparable growth. For September–December only, sales increase from 26,415,255.51 to 36,157,519.26 and profit from 3,878,464.51 to 5,435,484.26. Use these matched periods for year-over-year interpretation.

## Recommended follow-up

| Decision | Evidence | Next analysis | Proposed measure of success |
| --- | --- | --- | --- |
| Review Enterprise terms | -3.13% segment margin | Loss concentration by product, country and discount band | Reduced loss without disproportionate lost profitable volume |
| Evaluate discount approval rules | Lower observed margins in high-discount records | Compare within product/segment/country and test any rule change | Incremental contribution, with a control group |
| Protect profitable product mix | Paseo leads total profit; Amarilla leads margin | Demand, capacity and customer mix review | Contribution after incremental operating costs |
| Improve management comparisons | Incomplete 2013 coverage | Matched-month and seasonality analysis | Consistent reporting window and signed-off definitions |

These are proposed actions. No business intervention or measured commercial improvement is claimed.

## Validation and limits

`scripts/analyze.py` validates all rows against Gross Sales - Discounts = Sales, Sales - COGS = Profit, and Units Sold × Sale Price = Gross Sales. It checks year/month fields against Date and reconciles sales, profit and discounts independently with SQLite. It preserves the literal `None` discount-band category and trims whitespace from headers and categories. Margins use ratios of totals, not averages of row percentages.

The sample has no customer or order keys, no marketing costs or overhead, and only 16 months of history. Profit is the source's sales-minus-COGS measure, not audited net income. Historical sample data supports a dashboard demonstration rather than a current forecast.

Source: [Microsoft Financial Sample](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-financial-download). The analysis outputs include a SHA-256 checksum to identify the downloaded workbook version.
