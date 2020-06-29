## Alcohol Excise tracking for Odoo
 
 ### Introduction

This app has been developed to help users of Odoo who work with alcoholic beverages track their excise liability.

The UK legislation is laid down in [HMRC notice 226](https://www.gov.uk/government/publications/excise-notice-226-beer-duty/excise-notice-226-beer-duty--2). Other EU countries work under similar rules.

This software is Free and Open source.
### Installation

You must have the Inventory (stock) module installed before you install the Excise module. Clone the repository into the custom add-ons folder defined in your Odoo configuration file. After updating your Apps list the Excise-Alcohol app will become available for installation.

  

### Setup

Under Inventory – Configuration – Excise (Excise Categories) you can set up the categories of alcoholic beverages you work with. The installation process will populate this list with the UK categories defined [here](https://www.gov.uk/government/publications/rates-and-allowance-excise-duty-alcohol-duty/alcohol-duty-rates-from-24-march-2014).

  

![](https://kodoo.co.uk/web/image/1265/1.png)  

  

If you operate a bonded warehouse you can enter your warehouse number on the Warehouse screen.

The presence of a warehouse number tells the system that the location stores product duty-unpaid.

![](https://kodoo.co.uk/web/image/1266/2.png)  

  

If you have a duty paid area within your warehouse (e.g. a returns area) you should set this up as a location. (enable the setting Storage Locations). Check the “Duty Paid Location” setting to indicate that this location stores Duty paid stock within an otherwise duty free warehouse.

![](https://kodoo.co.uk/web/image/1267/3.png)  

  

The system will calculate duty when moving stock from a duty-unpaid location to a duty-paid location. The system will prohibit moving excisable stock from a duty paid location to a duty unpaid location.

  

### Product Setup

![](https://kodoo.co.uk/web/image/1268/4.png)  
  

On the Excise tab of the Product card select Track Excise if Excise should be calculated. Enter the ABV and select the relevant Category. Enter the volume of product for excise purposes in Litres.

If you use attributes to specify packaging you can specify the Excisable volume of the product at variant level.

### Reporting

Under the reporting menu look at the Excise moves.

![](https://kodoo.co.uk/web/image/1269/5.png)  

An Excise move is created per movement per excise category. If the category has an additional category (High-streingth beer) then two excise move records will be created.

You can view these Excise moves either grouped or in a pivot. Use standard Odoo filtering to assist the completion of returns.
