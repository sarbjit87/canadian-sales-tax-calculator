# canadian-sales-tax-calculator
REST API for calculating Canadian Sales Tax based on province

#INSTALLATION#

##USING DOCKER##

If you have Docker & Docker-Compose installed on your system

`git clone https://github.com/sarbjit87/canadian-sales-tax-calculator.git`
`docker-compose up -d --build`
`Visit http://127.0.0.1:8002/docs/ to for the API documentation`

##Python traditional approach##

`git clone https://github.com/sarbjit87/canadian-sales-tax-calculator.git`
`pip -r requirements.txt`
`Visit http://127.0.0.1:8002/docs/ to for the API documentation`

#API Documentation#

API Endpoint                   | HTTP Method   | Result
-------------                  | ------------- | -------------
/get-province-codes/           | GET           | Returns the code for all the provinces, e.g. ON for Ontario
/get-tax-rate/all/             | GET           | Returns the tax-rate (GST, PST, Total-Tax) for all the provinces
/get-tax-rate/{province-code}/ | GET           | Returns the tax-rate (GST, PST, Total-Tax) for the individual province
/get-tax/                      | POST          | Returns the tax on the total price for individual province

e.g. /get-tax/ with the request-body as
{
  "price": 10.54,
  "province": "QC"
}

curl -X POST "http://127.0.0.1:8002/get-tax/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"price\":10.54,\"province\":\"QC\"}"

will return

{
  "price": 10.54,
  "province": "QC",
  "total_tax_percentage": 14.975,
  "gst": 5,
  "pst": 9.975,
  "tax_amount": 1.58,
  "price_with_tax": 12.12
}

**Source for tax-rates**

Tax-rates are copied/referenced from the website https://canadabusiness.ca/government/taxes-gst-hst/federal-tax-information/overview-of-charging-and-collecting-sales-tax/?it=eng/page/2651/

**DISCLAIMER**

THE CODE IS BEING PROVIDED FOR INFORMATIONAL PURPOSES ONLY.

USE ON YOUR OWN RISK. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER OR CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES

THIS REPO IS RELEASED WITH NO WARRANTY AT ALL.
