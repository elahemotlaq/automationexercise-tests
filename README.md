# AutomationExercise E2E Test

This project contains an **end-to-end automated test** using **Selenium + Pytest** for [automationexercise.com](https://automationexercise.com).
It covers the full user flow: **Signup → Login → Add to Cart → Logout**.

---

## Requirements

* Python 3.8+
* Google Chrome
* Matching ChromeDriver

Install dependencies:

```bash
pip install selenium pytest
```

---

## Run Test

```bash
pytest -v test_end_to_end.py
```

---

## Output

After running the test, results are saved in `test_results.txt`:

```
Test Case 1: Signup Passed successfully
Test Case 2: Login Passed successfully
Test Case 12: Products added to cart successfully
Test Case 4: Logout Passed successfully
```

---

**Author:** Elahe Motlagh
**Tools:** Selenium | Pytest | ChromeDriver
