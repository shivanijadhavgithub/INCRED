import asyncio
import calendar
from asyncio import sleep


import playwright
from playwright.async_api import Playwright, async_playwright, expect

lead_values = {
"loan_category":"Un Secured",
"loan_type":"Personal Loan",
"loan_amount":100000,
"zip_url":"url",
"applicant_count":1,
"applicant1":{
    "mobile_num":9730570991,
    "pan_number":"DHEPM8568R",
    "personal_mail_id":"shivani@gmail.com",
    "gender":"Male",
    "dob":"03-11-1995",
    "employment_type":"",
    #"current_residence_type":"",
    #"current_residence_pincode":"",
    #"house_no":"",
    #"building_name":"",
    #"street_name":"",
    #"nearest_landmark":"",
    #"gmail" : "hhiud798@gmail.com",
},
"residence_details":{
      "res_street": "",
      "res_area": "semangi",
      "res_landmark": "",
      "res_pincode": "",
      "res_area": "",
      "res_type": ""
},
"other_details":{
    "house_no":"",
    "res_date":"",
    "dsa":"",
    "dst":"",
    "branch":""

}

}
async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    context = await browser.new_context()
    page = await context.new_page()

    # dateofbirth = lead_values["applicant1"]["dob"]
    # splittext = dateofbirth.split("/")
    # print(dateofbirth)
    # date =

    await page.goto("https://sales.incred.com/web/#/sales/plInsta/login")
    await page.locator('[placeholder="your-email@incred.com"]').fill("deepak.m@finwizz.net")
    await page.locator('[id="Btn"]').click()
    otp = input("Enter OTP: ")
    await page.locator('[class="auth0-lock-input auth0-lock-input-code"]').fill(otp)
    await page.locator('[id="Btn"]').click()
    await page.locator('[id="newApplication"]').click()
    await page.locator("text=PL - Instant Personal Loan").click()
    await page.locator('[name="MOBILE"]').fill(str(lead_values["applicant1"]["mobile_num"]))
    await page.locator('[name="PAN"]').fill(lead_values["applicant1"]["pan_number"])
    await page.locator("text=Send OTP ").click()
    await page.locator("text=Proceed").click()
    otp = input("Enter second OTP: ")
    await page.locator('[name="OTP"]').fill(otp)
    await page.locator("text=Continue ").click()
    await sleep(3)
    await page.locator("text=Personal Email ID").fill(lead_values["applicant1"]["personal_mail_id"])
    if lead_values["residence_details"]["gender"] == "Female":
        await page.locator('[ng-reflect-value="F"]').click()
    elif lead_values["residence_details"]["gender"] == "Male":
        await page.locator('[ng-reflect-value="M"]').click()
    dob = lead_values["residence_details"]["dob"].split("-")
    day = dob[0]
    month = dob[1]
    year = dob[2]

    await page.locator('[class = "datepicker-switch"]').click()
    await page.locator('[class = "datepicker-switch"]').click()

    if int(year)>=1989 and int(year)<1999:
        await page.locator('[class="prev"]').click()
        await page.locator(f"text = {year}").click()

    elif int(year) >= 1979 and int(year) < 1989:
        await page.locator('[class="prev"]').click()
        await page.locator('[class="prev"]').click()
        await page.locator(f"text = {year}").click()

    elif int(year) >= 1969 and int(year) < 1979:
        await page.locator('[class="prev"]').click()
        await page.locator('[class="prev"]').click()
        await page.locator('[class="prev"]').click()
        await page.locator(f"text = {year}").click()
    else:
        await page.locator(f"text = {year}").click()


    await page.locator(f"text = {calendar.month_abbr[month]}").click()
    await page.locator('[class="day"]').nth(int(day) - 1).click()




    # await page.locator('[id="dateofbirth"]').click()
    # await page.locator('[class="datepicker-switch"]').nth(0).click()
    # await page.locator('[class="datepicker-switch"]').nth(1).click()
    # dateofbirth = lead_values["applicant1"]["dob"]
    # splittext = dateofbirth.split("/")
    # print(dateofbirth)
    # date=splittext[0]
    # if int(date)>10:
    #     dateintext=date
    #     print(dateintext)
    # else:
    #     date1=date.split("0")
    #     dateintext=date1[1]
    #     print(dateintext)
    #
    # month=splittext[1]
    # if int(month)>10:
    #     monthintext=month
    #     print(monthintext)
    # else:
    #     month1=month.split("0")
    #     monthintext=month[1]
    #     shortmonth=calendar.month_abbr[int(monthintext)]
    #     fullmonth=calendar.month_name[int(monthintext)]
    #     print(shortmonth)
    # year=splittext[2]
    # fulldateintext=fullmonth+" "+dateintext+","+" "+year
    # print(fulldateintext)
    # if(int(year)<=1995 and int(year)>=1960):
    #     await page.locator('[class="prev"]').click()
    #     await page.get_by_text(year).click()
    #     await page.get_by_text(month).click()
    # if lead_values["employment_type"] == "salaried":
    #     await page.locator("ng-reflect-value=SALARIED").click()
    # else:
    #     await page.locator("ng-reflect-value=SELFEMP").click()

    await page.locator('[name="RESIDENCE_TYPE"]').fill(lead_values["residence_details"]["res_type"])
    await page.locator('[name="CURRENT_RESIDENCE_PINCODE"]').fill(lead_values["residence_details"]["res_pincode"])
    await page.locator('[name="HOUSE_NO"]').fill(lead_values["residence_details"][""])
    await page.locator('[name="BUILDING_NAME"]').fill(lead_values["residence_details"]["res_area"])
    await page.locator('[name="STREET_NAME"]').fill(lead_values["residence_details"]["res_street"])
    await page.locator('[name="LANDMARK"]').nth(0).fill(lead_values["residence_details"]["res_landmark"])

    
    await page.locator('[class="multiple dsa-lbl-cls"]').nth(0).click()
    await page.locator("text=Pune - FINWIZZ FINANCIAL SERVICES PVT LTD").click()
    await page.locator('[class="multiple dsa-lbl-cls"]').nth(1).click()
    #await page.locator("")
    await page.locator('[class="multiple dsa-lbl-cls"]').nth(2).click()
    await page.locator('[value="PUNE"]').click()
    await page.locator('[id="CONFIRMATION"]').check()
    await page.locator("text=Continue").click()
    await context.close()
    await browser.close()

async def main()->None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())


