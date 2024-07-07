import asyncio
import json 
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright

# load test cases from JSON file
with open('testCases.json') as f:
    test_cases = json.load(f)

@pytest_asyncio.fixture(scope="function")
async def launch_page():
    async with async_playwright() as playwright:
        print("Launching browser...")
        browser = await playwright.chromium.launch(headless=False)  
        page = await browser.new_page()
        await page.goto("https://app.asana.com/-/login")
        await page.wait_for_load_state()
        print("Page loaded:", page.url)
        yield page

        print("Closing page and browser...")
        await page.close()
        await browser.close()


@pytest.mark.asyncio
async def test_get_started_link(launch_page):
    page = launch_page  # Obtain the page object from the fixture

    # Perform actions on the page
    print("Filling email address...")
    await page.get_by_label("Email address").fill("ben+pose@workwithloop.com")
    
    print("Clicking 'Continue' button...")
    await page.click("div.ThemeableRectangularButtonPresentation--isEnabled.ThemeableRectangularButtonPresentation.ThemeableRectangularButtonPresentation--large.LoginButton.LoginEmailForm-continueButton:has-text('Continue')")
    await page.locator('.LoginPasswordForm-passwordInput').fill("Password123")
    await page.click("div.ThemeableRectangularButtonPresentation--isEnabled.ThemeableRectangularButtonPresentation.ThemeableRectangularButtonPresentation--large.LoginButton.LoginPasswordForm-loginButton:has-text('Log in')")
    
    #Click on the Cross Functional project tab
    await page.get_by_label("Cross-functional project plan, Project").click()
    await page.wait_for_load_state()


    for case in test_cases:
        print(f"Navigating to: {case['leftNav']}")
        await page.wait_for_selector(f'text="{case["leftNav"]}"', timeout=30000)
        await page.click(f'text="{case["leftNav"]}"')
        await page.wait_for_load_state()

        # Verify the card is within the right column
        print(f"Verifying card title '{case['card_title']}' in column '{case['column']}'")
        column = f'text="{case["card_title"]}"'
        await page.wait_for_selector(column, timeout=30000)
        card = page.locator(column)
        count = await card.count()
        assert count >= 1, f"Expected one card with title '{case['card_title']}', but found {count}"

        cards = card.first
        assert await cards.is_visible(), f"Card title '{case['card_title']}' not found in column '{case['column']}'"

        print(f"Clicking on card '{case['card_title']}'")
        await cards.click()
        await page.wait_for_load_state()

    print("All test cases completed successfully.")

