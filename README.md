## Asana Technical Assessment 

### Challenges & Solutions
- Loading State Issues
One of the significant challenges I encountered was the website taking too long to load, causing the assertions to fail. To address this, I utilized Playwright's await page.wait_for_load_state() method to ensure that the page was fully loaded before proceeding with the next steps in the test. This adjustment helped in synchronizing the test flow with the website's loading time, ensuring that elements were present before any actions were performed.

- Asynchronous Handling
Initially, I faced issues with running everything asynchronously rather than relying on Playwright's regular synchronous API. This was primarily due to my lack of prior knowledge of Playwright before this assessment. However, learning Playwright and navigating through its documentation helped me overcome these issues. Adapting to Playwright's asynchronous nature was crucial in writing effective and efficient tests.

- Assertions Failing
The assertions were failing because the website elements were not loaded in time. By implementing await page.wait_for_load_state(), I was able to mitigate this issue, ensuring that the elements were available for interaction and verification. This was a critical adjustment that allowed the tests to run smoothly and accurately.

- Navigation Based on JSON Data
Obstacle: Implementing navigation based on the leftNav field in the JSON object required dynamically generating selectors and ensuring accurate page transitions.
Solution: Utilized Playwright's flexible locator generation capabilities to create dynamic locators based on the leftNav data. This ensured the tests could navigate to the correct project pages as specified in each test case.

- Verifying Card Titles in Specific Columns
Obstacle: Verifying that a specific card title exists within a designated column involved accurately locating elements within the page structure and handling cases where multiple similar elements might exist.
Solution: Implemented precise locators to target the specified columns and card titles. Used Playwright's isVisible method to confirm the presence of the card title in the correct column, ensuring robust validation.

### Recommendations
1. Improved Test Coverage
Expand the JSON data to include additional test cases covering various projects, columns, and card titles. This will enhance the comprehensiveness of the tests and ensure broader coverage of potential scenarios.

2. Enhanced Error Reporting
Integrate detailed error reporting and logging mechanisms, such as capturing screenshots on failure and generating HTML reports using pytest-html. This will facilitate easier debugging and analysis of test failures.

3. Parallel Test Execution
Utilize pytest-xdist for parallel test execution, reducing the overall test runtime and improving efficiency. This is particularly beneficial for large test suites with numerous test cases.

4. Regular Maintenance
Ensure regular updates and maintenance of the test suite to accommodate any changes in the Asana's website or project structures. This will help maintain the accuracy and relevance of the tests over time. Potentially even adding a CI for continous deployments that can run every day.