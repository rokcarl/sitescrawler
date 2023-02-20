# Ceecee

Ceecee is an app to gather information on your customer's customers. Hence the
name.

## Running

To run the application, first run `make build` to install the needed
requirements, then you can run it with `make run`.

The result will be output to `data` directory.

## Possible improvements

* Make sure the company name is correct and properly capitalized.
* Extend the parsing to companies from other subpages like https://scale.com/customers
  and https://www.deel.com/case-studies.

## Example run

```bash
❯ make run
python main.py
Crawling Scale...
                       Microsoft: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmicrosoft.svg&w=256&q=100
                            Brex: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fbrex.svg&w=256&q=100
                            Etsy: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fetsy.svg&w=96&q=100
                        Flexport: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fflexport.svg&w=256&q=100
                  General-Motors: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fgeneral-motors.svg&w=96&q=100
                       Instacart: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Finstacart.svg&w=256&q=100
                            Meta: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fmeta.svg&w=256&q=100
                             Sap: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fsap.svg&w=128&q=100
                          Square: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Fcustomer-logos%2Ffff%2Fsquare.svg&w=256&q=100
                          Toyota: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Ftoyota.svg&w=256&q=100
                        Airforce: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fairforce.svg&w=96&q=100
                          Usarmy: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fusarmy.svg&w=96&q=100
                          Openai: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Fcustomers%2Fopenai.svg&w=256&q=100
                           Adept: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Finvestors%2Fadept.png&w=256&q=100
                          Carper: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Finvestors%2Fcarper.png&w=256&q=100
                          Cohere: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Finvestors%2Fcohere.svg&w=256&q=100
                       Stability: https://scale.com//_next/image?url=%2Fstatic%2Fimages%2Flogos%2Finvestors%2Fstability.png&w=256&q=100
Crawling Deel...
                            Nike: https://www.deel.com/hubfs/nike.svg
                         Dropbox: https://www.deel.com/hubfs/dropbox.svg
                         Shopify: https://www.deel.com/hubfs/shopify.svg
                      Forever 21: https://www.deel.com/hubfs/Forever_21_logo%201.svg
                          Reebok: https://www.deel.com/hubfs/Reebok_Logo_2019%201.svg
                        Intercom: https://www.deel.com/hubfs/intercom-logo-white.svg
                          Notion: https://www.deel.com/hubfs/Deel/Images/Logo-notion.svg
                         Revolut: https://www.deel.com/hubfs/Revolut-Logo.white.svg
                          Subway: https://www.deel.com/hubfs/Subway_2016_logo%201.svg
                          Reddit: https://www.deel.com/hubfs/Reddit.svg
                    Calvin Klein: https://www.deel.com/hubfs/Calvin%20Klein.svg
                        Red Bull: https://www.deel.com/hubfs/Red%20Bull.svg
                          Zapier: https://www.deel.com/hubfs/Zapier.svg
Crawling Webflow...
                            Dell: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b549e0b747857d92225_logo-dell.svg
                  Bain & Company: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b54c589e180f3c82b0e_logo-bain.svg
                         Zendesk: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b54c589e19a85c82b0d_logo-zendesk.svg
                         Rakuten: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b5436c9b6e53e0b7327_logo-rakuten.svg
                   Pacific Funds: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b5480fb346b8f51271b_logo-pacific-funds.svg
                         Discord: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b5497ebc038008bb30d_logo-discord.svg
                             NCR: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b54d627525b03579446_logo-ncr.svg
                         Lattice: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b546f9d88f3cc8c13b9_logo-lattice.svg
                             TED: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/618b3b54f2b89ac9cfac0425_logo-ted.svg
                            Vice: https://assets-global.website-files.com/5d3e265ac89f6a3e64292efc/62ed8a35043a3640cce05dfb_logo-vice-white.svg
```