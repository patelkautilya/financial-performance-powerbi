let
 Source = Excel.Workbook(Web.Contents("https://download.microsoft.com/download/1/4/E/14EDED28-6C58-4055-A65C-23B4DA81C4DE/Financial%20Sample.xlsx"), null, true),
 Financials = Source{[Item="financials", Kind="Table"]}[Data],
 CleanNames = Table.TransformColumnNames(Financials, Text.Trim),
 Types = Table.TransformColumnTypes(CleanNames, {{"Segment", type text}, {"Country", type text}, {"Product", type text}, {"Discount Band", type text}, {"Units Sold", type number}, {"Manufacturing Price", Int64.Type}, {"Sale Price", Int64.Type}, {"Gross Sales", type number}, {"Discounts", type number}, {"Sales", type number}, {"COGS", type number}, {"Profit", type number}, {"Date", type date}, {"Month Number", Int64.Type}, {"Month Name", type text}, {"Year", Int64.Type}}),
 CleanText = Table.TransformColumns(Types, {{"Segment", Text.Trim, type text}, {"Country", Text.Trim, type text}, {"Product", Text.Trim, type text}, {"Discount Band", Text.Trim, type text}, {"Month Name", Text.Trim, type text}}),
 Month = Table.AddColumn(CleanText, "Year Month", each Date.ToText([Date], "yyyy-MM"), type text)
in
 Month
