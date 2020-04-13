from fastapi import FastAPI
from pydantic import BaseModel
import enum
import json

def _readProvinceTaxRate():
    with open('/src/app/sales_tax.json') as f:
        data = json.load(f)
    return data

def _readProvinceCodes():
    with open('/src/app/province_codes.json') as f:
        data = json.load(f)
    return data

province_codes = _readProvinceCodes()
province_sales_tax = _readProvinceTaxRate()

ProvinceName = enum.Enum("ProvinceName", province_codes, type=str)

class SalesTax(BaseModel):
    price: float
    province: ProvinceName

app = FastAPI()

# Return the list of Province Names with abbreviation codes
@app.get("/get-province-codes")
def get_province_codes():
    return province_codes

# Return the sales-tax for all the provinces
@app.get("/get-tax-rate/all")
def get_all_province_rate():
    return province_sales_tax

# Return the sales-tax for the individual province
@app.get("/get-tax-rate/{province_code}")
async def get_province_rate(province_code: ProvinceName):
    retData = province_sales_tax[province_code.name]
    retData['PROVINCE'] = province_code.name
    return retData

# Return the sales-tax for the total price provided for individual province
@app.post("/get-tax/")
async def get_province_sales_tax(sale: SalesTax):
    sale_dict = sale.dict()
    province_data = province_sales_tax[sale.province.name]
    sale_dict["total_tax_percentage"] = province_data['TOTAL']
    sale_dict["gst"] = province_data['GST']
    sale_dict["pst"] = province_data['PST']
    tax_amount = (sale_dict["total_tax_percentage"] * sale.price)/100
    sale_dict["tax_amount"]  = float("{:.2f}".format(tax_amount))
    sale_dict['price_with_tax'] = sale.price + sale_dict["tax_amount"]
    return sale_dict
