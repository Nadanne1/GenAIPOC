<a id='8961f93b-bc95-47ba-b02f-9658938c303a'></a>

STAFF
---
REPORTS

<a id='90cee7b0-dfa4-42e0-8c66-c707ef5a36e6'></a>

NO. 1143
MARCH 2025

<a id='47d597e9-eff2-4d85-b5d6-a81039427e98'></a>

Credit Card Banking

<a id='e97ad5e3-6220-4300-bb85-b3488426faf1'></a>

Itamar Drechsler | Hyeyoon Jung | Weiyu Peng
Dominik Supera | Guanyu Zhou

<a id='871042f1-5034-46b2-9f2b-a4556f307ce5'></a>

FEDERAL RESERVE BANK of NEW YORK

<a id='9e624af8-2462-4aec-9969-740f4fc5d0c0'></a>

**Credit Card Banking**
Itamar Drechsler, Hyeyoon Jung, Weiyu Peng, Dominik Supera, and Guanyu Zhou
*Federal Reserve Bank of New York Staff Reports, no. 1143*
March 2025
https://doi.org/10.59576/sr.1143

<a id='3104dc03-e741-4b8f-b147-7fe5450aece7'></a>

# Abstract
Credit card interest rates, the marginal cost of consumption for nearly half of households, currently average 23 percent, far exceeding the rates on any other major type of loan or bond. Why are these rates so high? To understand this, and the economics of credit card banking more generally, we analyze regulatory account-level data on 330 million monthly accounts, representing 90 percent of the US credit card market. Default rates are relatively high at around 5 percent, but explain only a fraction of cards' rates. Non-interest expenses and rewards payments are more than offset by interchange and non-interest income. Operating expenses, such as marketing, are very large, and are used to generate pricing power. Deducting them, we find that credit card lending still earns a 6.8 percent return on assets (ROA), more than four times the banking sector's ROA. Using the cross section of accounts by FICO score, we estimate that credit card rates price in a 5.3 percent default risk premium, which we show is comparable to the one in high-yield bonds. Adjusting for this, we estimate that card lending still earns a 1.17 percent to 1.44 percent "alpha" relative to the overall banking sector.

<a id='a34ff847-4c45-4c2a-86db-134b9f0f32b6'></a>

JEL classification: G12, G21, G51
Key words: credit cards, banking, asset pricing, household finance

<a id='26648c47-5705-4685-a7ea-5ab78ada1f92'></a>

Jung: Federal Reserve Bank of New York (email: hyeyoon.jung@ny.frb.org). Dreschsler, Peng, Zhou:
University of Pennsylvania (emails: idrechsl@wharton.upenn.edu, weiyupen@wharton.upenn.edu,
guanyuz@wharton.upenn.edu). Supera: Columbia Business School (email: ds3791@columbia.edu).
The authors thank seminar participants at Wharton, the Federal Reserve Bank of New York, and the
Federal Reserve Bank of Philadelphia for helpful comments. They also thank Robert Hammer for his
valuable insights.

<a id='8fd6a108-52ba-44b6-8040-e3004c5144f9'></a>

This paper presents preliminary findings and is being distributed to economists and other interested readers solely to stimulate discussion and elicit comments. The views expressed in this paper are those of the author(s) and do not necessarily reflect the position of the Federal Reserve Bank of New York or the Federal Reserve System. Any errors or omissions are the responsibility of the author(s).

<a id='0524dc8c-9f75-4741-8109-729b6f18392f'></a>

To view the authors' disclosure statements, visit
https://www.newyorkfed.org/research/staff_reports/sr1143.html.

<a id='f164349a-4ea9-4869-8eaf-235b9fb26a3c'></a>

# 1 Introduction
Credit cards are one of the most commonly used financial products in the United States.
There are around 580 million credit card accounts nationwide, with approximately 74% of
US adults have a credit card account in their name.¹ Credit cards are now the primary
method of payment for consumers, with total purchase volume of $6 trillion in 2023, or 70%
of retail spending.²

<a id='8190b63e-667a-455e-8828-5daebcbacd6f'></a>

Credit cards are also the main form of consumer unsecured borrowing, making it the primary source of marginal buying power for nearly half of households. Indeed, 60% of all credit card accounts are borrowers, defined as carrying a balance from one month to the next. Thus, for the majority of cardholders the cost of substituting consumption over time is given by the interest rate on their credit card, not the rate on a savings account or treasury bill, as often assumed in macroeconomic models. This makes a big difference because credit card interest rates are very high: the average annual percentage rate (APR) on general purpose credit cards in 2023 was 23%, a spread of 18% over the average Fed funds rate.

<a id='3c2bbf30-cb19-4f89-977b-5ec8c127060c'></a>

This interest spread is far higher than that on other loans or bonds. For comparison,
the spread of rates on Commercial and Industrial (C&I) loans (loans to firms) over the Fed
funds rate averaged 2.25%, the spread of mortgage rates over treasuries was 3%, and the
spread of high-yield US corporate bonds-the riskiest corporate bonds-over treasuries was
4.21%.

<a id='18bfb1ab-75ac-4828-9640-e82f797701bf'></a>

This leads us to ask two questions in this paper. First, why are credit card rates so high?
We analyze credit card lending as an asset class and compare its pricing to that of other types of lending. At the same time, credit card banking is an intensely retail business, a potentially important factor in understanding credit card rates. Thus, our second aim is to

1See Consumer Financial Protection Bureau – Consumer Credit Card Market Report (October 2023).
2We compute the total purchase volume based on Nilson Report - Top US General Purpose Credit Card Issuers at Midyear (September 2023). The total retail sales and food services spending in the US were obtained from United States Census Bureau – Advance Monthly Sales for Retail and Food Services.

<a id='3076fb0e-bc08-4da5-a977-b074c388b987'></a>

1

<a id='91b3985f-2373-40e3-b6fa-2b157dd66f24'></a>

understand the economics of the business of credit card banking. We therefore investigate all the streams of revenues and costs involved in this business, and whether market power plays an important role in them. This helps to provide a fuller answer to our first question.

<a id='b5252135-a1ad-41b9-bc0a-df17fa1b6891'></a>

Despite their high interest rates, consumers borrow substantial amounts on credit cards.
As of the end of 2023, outstanding credit card balances were $1.1 trillion. Of this, 85% was
due to borrowers, with the rest due to "transactors", accounts that repay their balance by
the end of the statement period. Although these balances are economically sizable, they
accounted for only a modest 4.5% of banks' balance sheets during the period 2010 to 2023.
Yet, because of their high interest rates, they generated 16.6% of banks' interest income on
average during the same period.

<a id='fc783ade-dcec-4c7b-be5c-fb9be30d3325'></a>

Credit card lending is personal lending and unsecured, making it banks' riskiest type of lending. From 2010 to 2023, credit card charge-offs averaged 3.96% of total balances, compared to only 0.46% and 0.43% for business loans and residential mortgages, respectively. As a result, on average 53% of banks' annual default losses were due to credit card lending. Credit card default losses are large enough to be comparable to those on corporate bonds, despite there being ten times as much corporate bonds outstanding as credit card balances. Specifically, annual default losses on credit cards were on average 64% of those on corporate bonds during 2010 to 2023, assuming a standard 50% recovery rate on corporate bonds.3

<a id='58b92f67-c5a7-4b5f-a9f9-d33db7556023'></a>

We analyze four potential explanations for why credit card rates are so high. The first is that they are compensation for average default losses. The second is that they are required to cover the high cost of credit card "rewards", which banks pay their customers in cash or airline miles. The third is that credit card rates price in a large default risk premium, because default risk is undiversifiable and default losses are high in bad economic states.

3Corporate bond default amounts are from S&P Global Annual U.S. Corporate Default And Rating Transition Study (2023).

<a id='3f579d1e-bb55-4185-83f0-7dae10331379'></a>

2

<a id='e087c725-0f82-451d-8651-2b9ec281b71c'></a>

The fourth is that banks are able to charge high rates due to market power.<sup>4</sup> Market power and risk pricing can also interact, if banks price a higher default risk premium into credit card rates than prevails in other markets.

<a id='bba92ab3-709c-47ea-baa4-d807959be125'></a>

Our analysis utilizes a comprehensive supervisory dataset on credit card accounts from the Federal Reserve's Y-14M reports. This dataset contains monthly data on approximately 330 million individual credit card accounts from the 20 largest banks, covering more than 90% of credit card lending in the US. It contains detailed, account-level information, including the account holder's FICO score, the account's APR, credit limit, monthly balance, purchase volume, fees charged, rewards received, and the account holder's income and geo-graphic location. The data allows us to calculate the various components of revenues and expenses of credit card banking at the individual account level.

<a id='1af155d5-48cf-4189-8179-f2bfa8311c55'></a>

We track accounts over time in cohorts based on month of origination. This is important for calculating the lifetime returns on accounts because a card's APR spread (the spread of its APR over the Fed Funds rate) is effectively fixed at origination.5 Thus, in setting an account's APR spread, a bank must consider not only default risk in the near future, but over the account's whole life. By tracking accounts over time, we capture these future defaults in our measures of the returns banks make lending to these accounts.

<a id='b87ddbf6-5302-489e-a2a1-da3efb616e95'></a>

In order to have a sufficiently long time series to capture accounts' lifetime returns, we focus on the cohorts originated between January 2015 and December 2017, and track them until the end of our sample in December 2023. This gives us at least six years of data for each cohort. We sort the accounts in each cohort into portfolios by their FICO score at origination. FICO is the industry standard credit score. Its value ranges from 300 to 850, with a higher score indicating lower default risk.

<a id='43436148-ace4-41e9-bed0-62a927ac815c'></a>

⁴The literature has argued that the credit card market lacks competition (Ausubel, 1991; Herkenhoff and Raveendranathan, 2021), has high search or switching costs (Calem and Mester, 1995; Drozd and Nosal, 2008), and that consumers are heterogeneous in how intensely they search for the best rate (Stango and Zinman, 2016).

<a id='f3cf6f56-00b4-4291-8d3a-0279755fa903'></a>

5 This has been the case since the passage of the Credit CARD Act, which prohibits a bank from increasing an account's APR spread on existing borrowing. We show that in practice it is rare for an account's APR spread to change during its life.

<a id='b6e2913b-1cdb-438b-896e-b3d7644654c0'></a>

3

<a id='231a7fc2-6662-4bcc-ba2b-ae9d96cb0949'></a>

We sort accounts by their FICO at origination in order to obtain a large spread in their default risk. This also creates a large spread in their average APR, as FICO is the main variable banks use to set an account's APR. By tracking the revenues, costs, and defaults of these portfolios over time, we are able to analyze the risks and returns to credit card lending.

<a id='4bf5f821-01d4-4582-ae7d-c8780b9d9f6f'></a>

In each month, we further sort the accounts in the FICO portfolios into portfolios of borrowers and transactors. This is important because borrowers and transactors generate different risks and revenues. In the months an account is borrowing, it exposes the bank to default risk and is charged interest, unless it is in a zero-interest promotional period.<sup>6</sup> In the months that an account is a transactor, it poses no default risk and is not charged interest. We find that borrowers make up roughly 60% of active accounts, and that the borrower share of active accounts is strongly decreasing in FICO: for FICO scores above 800 it is slightly below 30%, but is over 65% for all FICO scores below 720, and rises to almost 80% for FICO scores near 600.

<a id='c2991bcb-c8e1-436b-a5f9-6c38c29eb86b'></a>

We begin by analyzing the interest rates that borrowers pay. Two main findings stand out. First, the average APR spread is high for all FICO scores, so even accounts with the highest possible FICO (850) pay an average APR spread of 7.2%. Second, the APR spread is strongly increasing in credit risk, rising to an average of 21% for 600 FICO accounts.

<a id='2788b710-fabf-472a-9cd1-7aa807fc92fb'></a>

To see if APR spreads are just compensation for expected default losses, we compare them to the average net charge-off rates (charge-offs net of recoveries) of the borrower portfolios. Since we track portfolios over a long time, we compute life-time averages of quantities by dividing the portfolio's cumulative dollar amount of the quantity over the sample period by the portfolios' cumulative monthly balance over the same period.

<a id='085a4cac-35b9-4f9a-aedd-d8f2df28e85a'></a>

We find that charge-off rates decrease almost linearly with FICO, from 9.3% per year at 600 FICO to 1.3% for 850 FICO. Although the charge-off rates are high, especially for
⁶Zero-interest promotional periods, typically offered to customers as an incentive to open a new account, usually take place within the account's first twelve months.

<a id='39fad92d-8ac0-41a7-abc2-79e12aeeec08'></a>

4

<a id='7da5a75d-7e2f-41db-b404-70790d2b82ff'></a>

the lower FICO scores, they are much lower than the corresponding APR spreads. Thus,
the APR spreads are mostly *not* compensation for expected default losses. Moreover, the
difference between the APR spread and charge-off rate, which we call the default-adjusted
APR spread, is increasing in default risk: from 6% at 850 FICO to 11.9% at 600 FICO.

<a id='fb830ca7-9c80-45fd-986b-f4dc0772d5e4'></a>

Next, we analyze the non-interest income and expense components of credit card banking to see how they affect profitability. Among these, the ones that are unique to credit cards are interchange income and rewards expenses. Interchange fees (also called "swipe" fees) are a percentage of a product's purchase price (around 2% usually) that is charged to the seller and split between the credit card network (Visa, Mastercard, American Express), the merchant's bank, and the customer's bank. Most of the fee is earned by the customer's bank. Rewards are a percentage of the purchase price that is paid to the customer (the cardholder) by their bank in return for paying with the card. Rewards are paid as cash, airline miles, or points that can be redeemed for cash or travel.

<a id='2798b846-fac5-4d76-b02e-57a97e039f75'></a>

The value of interchange and rewards has become very large. In 2023, the rewards expenses of the six largest card issuers totaled to an enormous $67.9 billion. Thus, it is plausible that banks charge high APR spreads to recoup these tremendous expenses. However, we find this is not the case. Rewards expenses are covered by banks' interchange income, with the two being closely intertwined. This is highlighted by the fact that banks' filings report the net of these two quantities as a single category. We find that banks' interchange income is 1.82% of purchase volume on average, while rewards costs are 1.57%.

<a id='02b6e5f2-4ddd-489a-8c5e-a07743353b67'></a>

Net interchange income as a fraction of balances differs greatly between borrowers and transactors. Because transactors repay their balance each month, they have substantially higher purchase volumes, and thus generate correspondingly higher net interchange income. They also have lower balances. We find that net interchange income is about 4.6% of balances for transactors, and 0.4% for borrowers. Net interchange income accounts for a large fraction of banks' return on assets (ROA) for transactors, but is a minor component for borrowers'. Nevertheless, net interchange is positive at all FICO scores for both transactors

<a id='2199f035-904d-403f-a05a-3abb1fcb2adf'></a>

5

<a id='09b8f4f6-4fca-4458-b8c8-1c2e6f8da679'></a>

and borrowers.

<a id='5f9a3b05-0c00-4139-bcb1-82f7bd38aeb9'></a>

We also analyze non-interchange fee income, which includes late fees, annual fees, and balance transfer fees. On average, accounts incur such fees of around 2.6% of their balances. Fee income is highest at the extreme ends of the FICO distribution: many high-FICO accounts pay large annual fees for premium credit cards, while many low-FICO customers pay substantial fees to transfer balances to new accounts.

<a id='4646ca76-2901-4ea3-8a97-3cfb7a2a92f9'></a>

Next, we analyze credit cards' operating expenses. Finance research often models banks as portfolios of financial assets and liabilities, and overlooks the influence that non-financial (i.e., operating) expenses have on their decisions. One of the main reasons commercial banks have high operating expenses is that they are in large part retail businesses.<sup>7</sup> We find that due to their intensely retail orientation, credit card operations have especially large operating expenses: 4-5% of balances annually. These costs explain about half of default-adjusted APR spreads.

<a id='5c95d737-b38d-4f56-810b-8a0077b790ed'></a>

A key reason that banks incur high operating costs is to obtain market power (i.e., a "franchise") (Drechsler, Savov and Schnabl, 2021a). This appears to be particularly true for credit card operations. We find that one of the largest components of their operating expenses is marketing. Credit card banks spend an average of 1-2% of assets each year on marketing, about 10 times the fraction spent by other banks. This is why the largest credit card banks, Capital One and American Express, are among the biggest marketers in the world, with marketing budgets as large as those of consumer products giants, and prolific advertisers, Nike and Coca-Cola. 8

<a id='4824f6f7-8349-4d67-8a8e-ebb3d5198dc2'></a>

We use the Y-14 data to analyze the relationship between credit card banks' operating expenses and their pricing power. An advantage of the Y-14 data is that the banks report the part of their total operating expenses that are spent on their credit card operations. We find

---

⁷Banks' retail dimension strongly influences their financial characteristics, such as the source and cost of their financing (e.g., deposits) and the assets they invest in (Drechsler, Savov and Schnabl, 2017, 2021a).
⁸In 2023, their marketing expenditures were as follows: Nike $4.1 billion, Coca-Cola $5 billion, Capital One $4 billion, and American Express $5.2 billion.

<a id='aea5a61b-b5ae-41aa-a2e6-365e28359295'></a>

6

<a id='f84b1376-87f2-4762-9279-a37ac5aa6a79'></a>

that there is large variation in spending on operating expenses per dollar of balances across banks. Moreover we show that a bank's operating expenses per dollar is strongly related to the interest spread and gross margin it earns on its borrowers at a given FICO score. This indicates that credit card banks have pricing power, and that their high operating expenses (and hence their high APRs) are in part due to the cost of maintaining it.

<a id='478fca4a-8caf-4f66-8f31-69caad0dc2e4'></a>

Combining all income and expenses, including operating expenses, we obtain the return on assets of the credit card portfolios. We find that ROA is high: 6.8% for the aggregate portfolio of borrowers, 2.57% for transactors, and 6.24% overall. Moreover, ROA is strongly increasing in borrowers' default risk, increasing from 5% for the high-FICO portfolios to nearly 11% for the low-FICO ones. Thus, ROA is strongly increasing in default risk, similar to what we found for default-adjusted APR. This suggests that credit card rates price in a default risk premium.

<a id='bc0d71dc-adf0-4ac6-a5e3-76878ee46e17'></a>

Two findings that we document support this hypothesis. The first is that charge-offs are highly correlated across FICO portfolios, rising together in cycles that peak during recessions. Hence, charge-off risk has a common component that cannot be diversified away within the credit card market. Second, credit card charge-off rates are highly correlated with default rates on both other bank loans and in the corporate bond market. Thus, default risk is also undiversifiable across other loan/bond markets. Since default risk has this undiversifiable (i.e., systematic) component, it is plausible that it is priced.

<a id='78de007d-2da7-466a-9394-26c18efc1a23'></a>

We test this by estimating a single-factor model of default risk using the cross-section of credit card portfolios.⁹ As a proxy for the systematic component of default risk, we use the change in the monthly charge-off rate of the aggregate credit card portfolio. We estimate the beta (exposure) of each FICO portfolio to systematic default risk by regressing the change in its monthly charge-off rate on the proxy. Following the standard asset pricing approach

<a id='c62bb890-0f1c-42ee-a5cb-eb2df8b6c008'></a>

9Credit cards are advantageous for analyzing the default risk premium because (a) of all the asset categories, they have the highest sensitivity to the default cycle, (b) they provide a large cross-section of sensitivities, and (c) there are millions of accounts, making it possible to precisely estimate portfolios' systematic default-risk exposures.

<a id='6909100c-c8b1-4b3b-972b-55a477921e36'></a>

7

<a id='fc2c8c88-5789-45bd-b335-0acaad5c577b'></a>

(Fama and MacBeth, 1973), we then estimate the compensation for default-risk exposure by regressing the portfolios' ROAs on their betas.
We find that the estimated charge-off betas are strongly and linearly decreasing in accounts' FICO scores. Thus, FICO score turns out to also be a good proxy for an account's beta to systematic charge-off risk. Regressing portfolios' ROAs on their betas, we estimate the risk premium on charge-off beta to be a highly significant 5.3% per year. We also find that the model's fitted portfolio ROAs are close to the actual ROAs across the whole range of FICO scores. Thus, exposure to aggregate default risk can fully explain the strong, decreasing relation between FICO score and ROA.

<a id='00beab1f-b367-4644-979a-1863c311e263'></a>

The intercept in the regression of ROA on charge-off beta is the ROA of hypothetical borrower with no systematic default risk (a zero-beta borrower). The estimated intercept is 2.41%. We can compare this estimate to the ROA for transactors, since they have a zero beta by construction, and were not included in the regression. The ROA of the transactor portfolio is 2.57%, similar to the zero-beta estimate.

<a id='3c349f50-1863-4e85-bf12-96966bfd489f'></a>

We then analyze how our estimated default risk premium compares to that in other markets. We focus on the corporate bond market because it is very large and its default rate is relatively sensitive to the default cycle. Mapping bonds' credit ratings to equivalent FICO scores, we find that historical risk premiums for BBB, BB and B rated bonds are very similar to the ROAs on their corresponding FICO portfolios. Thus, for most of their range corporate bonds and credit card rates appear to price in similar compensation for default risk. The exception are the lowest-rated bonds (CCC/C). In contrast to the linear relation between credit card risk premia and FICO score, our estimates of corporate bond risk premia are concave in their credit ratings. As a result, the risk premium of CCC/C-rated bonds is about 3% below that of comparably risky credit cards (620 FICO).

<a id='7263050a-14b9-45a4-8b1d-1f8459256095'></a>

Lastly, to estimate credit cards' "alpha" relative to the banking sector as a whole, we compare credit cards' zero-beta rate with the banking sector's ROA, adjusted for its small default risk using our risk premium estimate. The banking sector's pre-tax ROA is about

<a id='f61879aa-9e60-45bf-a39d-1835d9765b07'></a>

8

<a id='88a51ccc-8892-4950-8505-4a3911c0d9cf'></a>

1.5%, and we estimate its default risk premium to be 0.26%-0.53%, giving credit cards an alpha of between 1.17% and 1.44%.10

<a id='a1cede8a-a591-45df-aad8-b7f12b91849f'></a>

# Related Literature

Our paper contributes to the literature on bank profitability in credit card markets, including both academic studies and industry reports. The academic literature has primarily focused on the effects of the Credit Card Accountability Responsibility and Disclosure Act (CARD Act) on the cost of borrowing and bank profit components (Agarwal et al., 2015; Han, Keys and Li, 2018; Nelson, 2024). Agarwal et al. (2015) demonstrate that regulatory limits on credit card fees reduced overall lending income and bank profitability. They also document the key components of banks' realized average revenues, costs, and profits across FICO scores, focusing on the pre-CARD Act period that coincided with the Global Financial Crisis. Agarwal et al. (2022) study the distribution of rewards in various dimensions, including FICO, income, and geography, by comparing classic cards and reward cards. Their findings suggest that reward programs play a role in redistributing income from naïve to sophisticated consumers.

<a id='9bde3c51-9abb-4636-ac95-e90f0db0820c'></a>

We complement this literature in three key ways. First, rather than providing a point-in-time snapshot, as is common in previous studies and industry reports (e.g., Consumer Financial Protection Bureau, 2023), we are the first to analyze the lifetime profitability of credit card accounts over multiple years and provide a comprehensive breakdown of profit components in the cross-section of origination FICO scores. This approach is important for understanding the pricing of credit card APRs, because they are set at the time of origination, and are largely fixed due to the restrictions placed on banks by the CARD Act.
Second, we differentiate between borrowers and transactors, since they differ significantly

<a id='17ce422f-20ad-4f8f-9598-37db72c26b53'></a>

<sup>10</sup>The charge-off rate of the banking sector is around 0.25% of total assets (0.5% of loans and leases). Using the relationship between the average charge-off rate and default-risk betas estimated from the FICO portfolios implies that the banking sector has charge-off beta between 0.05 and 0.1, and hence a default-risk premium between 0.26% and 0.53%.

<a id='2159c03e-eeb4-4d78-aa57-a26f5a431c78'></a>

9

<a id='ecc6d37f-8ae2-41e9-91ed-59bf0fd40c24'></a>

in both the revenues and risks they generate for banks. Third, we are the first to estimate the default risk premium priced into credit card rates in the cross-section of FICO scores. We calculate the betas of accounts to the default cycle and risk-adjust the returns to lending to them.

<a id='54135eb4-a98a-494e-810f-3e4cccb47119'></a>

Our findings, based on the post-CARD Act period, show that the ROAs on credit card lending are large and decrease in accounts' FICO scores. Importantly, we find that the ROA for borrowers is much higher than that on transactors. However, the return on borrowers includes a substantial risk premium due to their their exposure to the credit default cycle.

<a id='0c145c18-053a-4ebd-a633-b113fb306445'></a>

More broadly, our paper contributes to the literature on the estimation of risk-adjusted returns in private markets (e.g., Kaplan and Schoar, 2005; Korteweg and Nagel, 2016; Gupta and Van Nieuwerburgh, 2021). While much of this literature has focused on private equity markets, more recent studies examine private credit markets, including corporate loans (Flanagan, forthcoming), collateralized loan obligations (Cordell, Roberts and Schwert, 2023), and private debt funds (Erel, Flanagan and Weisbach, 2024). We add to this body of work by analyzing credit card loans as an asset class.

<a id='cc4eed6b-56d8-4cc7-a830-c725cde436c5'></a>

Using the Fed's Y-14M reports, the most comprehensive and granular data set available on US credit card accounts, we are the first to estimate the returns, default-risk exposures and risk premia in credit card markets. Our analysis estimates credit card portfolio betas to the default cycle and uses these betas to estimate the default-risk premium. We are also the first to compare credit cards' default risk premium to that of the corporate bond market.

<a id='7b7238b4-d5db-4015-a619-4569bdaedc2b'></a>

Our findings reveal that credit card rates price in substantial risk premia, ranging from
1-2.5% for the highest FICO scores to 6.5-8.5% for the lowest ones. We compare these risk
premia to the default-adjusted credit spreads of speculative-grade bonds with comparable
default rates and find they are very similar for BBB, BB, and B rated bonds. However,
in the case of the riskiest bonds, rated CCC/C, we estimate the risk premium earned by
comparably risky credit cards (620 FICO) to be 3% higher. Fleckenstein and Longstaff
(2022) estimate the risk premia on credit card asset-backed securities (ABS), bonds backed

<a id='ea6958d2-aab8-452e-9b56-723bfc9830b1'></a>

10

<a id='e2d00f44-1576-44bc-a706-63c1afb066bf'></a>

by credit card cashflows. They estimate significantly lower risk premia, indicating that investors view credit card ABS as relatively safe. However, the risks of credit card accounts and credit card ABS cannot be compared directly because the ABS is over-collateralized to make it safer for investors.

<a id='4803cd04-8dfd-41dd-96e4-b7289af09b77'></a>

Finally, we contribute to the literature on competitiveness and market power in the
credit card market. Prior research has highlighted that this market is characterized by
limited competition (Ausubel, 1991; Herkenhoff and Raveendranathan, 2021), high search
and switching costs (Calem and Mester, 1995; Berlin and Mester, 2004; Drozd and Nosal,
2008; Galenianos and Gavazza, 2018; Nelson, 2024), and significant heterogeneity in con-
sumers' search intensity for the best rates (Stango and Zinman, 2016). We contribute to
this literature by highlighting a mechanism through which banks attain pricing power in the
credit card market: by incurring high operating costs, including large marketing expenses
and customer acquisition costs. As we show, banks that spend more on operating expenses
are able to charge substantially higher interest rates and earn larger gross margins from
borrowers with the same FICO scores. Our findings show that operating costs account for
approximately half of cards' default-adjusted APR spreads.

<a id='74aa666f-1572-498d-9edd-91c2de2ef531'></a>

These results also link our work to studies documenting banks' substantial market power in deposit markets (e.g., Neumark and Sharpe, 1992; Drechsler, Savov and Schnabl, 2017, 2021b). Banks pay significant fixed costs to maintain their deposit franchises, allowing them to charge substantial deposit spreads. Our findings highlight that credit card banks pay large fixed costs to earn substantial spreads on the lending side.

<a id='444149e6-1d5d-4844-b7d4-11fb9d252514'></a>

11

<a id='80ff7e37-0861-4101-a32e-995eb604b9c5'></a>

2 Data

<a id='5bc0adb8-5424-4b2d-86b1-881db60a8008'></a>

## 2.1 Y-14 Reports

We use a comprehensive and granular supervisory data set on credit card loans from the Federal Reserve's Y-14M reports. The data are collected for capital assessments and stress tests and contain monthly account-level information. All banks in the US with $100 billion or more in total consolidated assets are required to report the information. We focus on the reports' sub-schedule covering credit card loans. This data covers 20 banks, representing more than 90% of credit card lending in the US.

<a id='563121ad-104d-45a7-87ed-8dd17b85d34e'></a>

We use account-level variables, including the average percentage rate (APR), FICO score, balance, credit limit, purchase volume, and fees. Banks often provide special benefits to cardholders, such as lower introductory rates, reduced fees, or sign-up bonuses, and we observe these as well. We augment the account-level variables with variables reported as aggregates for portfolios of accounts. Portfolios are defined by the issuing bank, the type of credit card, and the type of lending.<sup>11</sup> Portfolio-level variables include interest expenses, rewards, interchange income, operating expenses, and fraud expenses. We use this information to calculate the profitability of the credit card business.

<a id='e3478b05-bde4-4d0c-80ea-16a60a059633'></a>

The bulk of our analysis focuses on consumer general-purpose reward credit cards. General purpose cards can be used at all merchants that accept credit cards and account for 90% of all US credit card lending. In contrast, private label cards can only be used at the retailer associated with the card.

<a id='409b6358-7eb2-479f-8842-16e4d8188591'></a>

We focus on accounts that originated between January 2015 and December 2017, and track them until December 2023, the end of our sample. Although the Y-14 data start in 2012, there are significant gaps in key variables before 2015. By restricting the sample to accounts originated by 2017, we ensure that the sample is long enough to assess the risk

11 There are four credit card types: general purpose, private label, business card, and corporate card. There are also four lending types: consumer bank card, consumer charge card, non-consumer card, and non-consumer charge card.

<a id='84ce791c-9dd5-4a94-9417-6a5999ea085b'></a>

12

<a id='2a31fa39-a471-4059-b4d4-256eeae5e4b6'></a>

and returns on these accounts over their life cycle. In robustness analysis, we confirm that
our findings are not sensitive to the choice of endpoints.

<a id='15ffaf67-b6ec-4862-85e4-1c9a42ebed27'></a>

For consistency, we restrict our sample to accounts that meet the following criteria: (1) observations begin within one month of the account's origination, (2) there are no missing data, and (3) if the account exits the dataset, the reason is specified as either charge-off or closure; otherwise, the account remains active until the end of our sample. In contrast to the usual practice of sampling the data, e.g., studying subsamples of 1% of observations, we analyze the entire data set. This gives us an average of 31 million observations per month for the period January 2015 to December 2023.

<a id='06bf57c8-3fc0-4392-9730-712bd0db9c82'></a>

## 2.2 Other Data Sources

**Call Reports** We complement the Y-14 data with bank call reports, which contain quarterly data on the income statements and balance sheets of all US banks. We use call reports to compare the profitability of credit card banks to other banks. We identify credit card banks as those in which (1) personal loans' share of assets exceeds 50%, and (2) at least 90% of personal lending is credit card lending. This definition follows from that used by the Federal Reserve's report to Congress on credit card banking.<sup>12</sup>

<a id='be8bd428-62ca-4773-9f34-28c211fc4a14'></a>

**Corporate Bond Data** We obtain data on corporate bond issues from the Mergent Fixed Income Securities Database (FISD). We use the data to compare the risks and returns of investing in corporate bonds with credit card lending. This data set contains information on a bond's issuance date, issue size, coupon rate, maturity date, and credit rating. 13 It also provides information that allows us to calculate the return to investing in the issue. In particular, we observe if the bond defaulted (and when), reached maturity and repaid its

12 The series of such reports are known as the "Report to the Congress on the Profitability of Credit Card Operations of Depository Institutions": https://www.federalreserve.gov/publications/credit-card- profitability.htm.
13 Ctondond and Doom's notinen tho nnimae coemen of anodit notinen [illegible]

<a id='b414c185-d225-4f99-9f3b-486ea92e5eb0'></a>

13 We use Standard and Poor's ratings as the primary source of credit ratings.

<a id='5ab1ccb3-ce42-4e6a-96be-2535320bedfd'></a>

13

<a id='661eddac-3a4f-47e2-bf75-bbe5c16874db'></a>

entire principal, or was called by the issuer.

<a id='4b5602c0-569f-4b73-9ced-ce11a7689e38'></a>

# 3 Overview

Table 1 panel A presents summary statistics for key income and expense components in credit card banking, based on data aggregated at the bank-month level from January 2015 until December 2023. Credit card banking is characterized by a high interest income rate, with an average interest spread - defined as the interest income rate minus the federal funds rate - of 14.2%. Charge-off rates are substantially smaller, averaging 5% across banks in the sample, with relatively low variation; the 25th percentile is 4%, and the 75th percentile is 5.3%. Recovery rates are low, averaging just 0.5%, or roughly one-tenth of charge-off rates. Interchange income and rewards expenses, reported as a share of assets to ensure comparability with net interest income, are both significant in magnitude. The average interchange income rate is 7.1% of assets, while rewards expenses amount to 4.8% of assets, making interchange income the larger of the two. Additionally, banks earn 2.1% of assets per year in non-interest income, with 1.7% coming from various fees. Operational costs represent the largest non-interest expense, averaging 4.9% of assets annually and varying significantly across banks. Other non-interest expense components are relatively small, with fraud-related expenses accounting for just 0.3% of assets per year.

<a id='48e3b487-65e5-4976-9f0b-ec710388a962'></a>

## 3.1 Borrowers and Transactors
A key distinction in credit card banking is whether an account is a transactor or a borrower (known as a "revolver" in industry terminology), in a given month. Transactors are accounts that repay their balance in full by the end of the statement month, whereas borrowers do not and hence borrow the unpaid amount from the bank. The distinction is important because a transactor does not pose a default risk to the bank and pays no interest. In contrast, a borrower exposes the bank to default risk and is charged interest. The exception

<a id='37277132-1b6a-4bdc-9d58-e6f4c5bcb82f'></a>

14

<a id='aa6def61-e719-4579-ab11-7dec85604ae2'></a>

is if the borrower is in a zero-interest promotional period. Such promotions are offered to prospective customers as an incentive to open a new account or transfer existing borrowing from another bank ("balance transfer"), with the promotional period typically occurring in the account's first twelve months.

<a id='6cccfb3d-a857-436e-8bff-85d07e0e57d7'></a>

Therefore, in each month, we classify each account as a transactor or borrower. We classify an account as a borrower if the account either repays less than its previous balance, incurs finance (i.e., interest) charges in the following month, experiences a charge-off, or transferred a balance from another account. All other accounts are classified as transactors.

<a id='3c8bb16c-0d51-4274-a458-b6c9fb80a3e7'></a>

Table 1 panel B reports summary statistics computed separately for borrowers and active transactors. There are several key differences between borrowers and transactors. Borrowers' average daily balance (ADB) is much larger on average than transactors. This is because borrowers' ADB includes both their current month's purchase volume and their past borrowing. Since transactors do not borrow, their ADB is due only to the current month's purchase volume. In contrast, transactors' purchase volume is larger than borrowers', in part because they are not encumbered by debt. Since interchange income and rewards payments are proportional to purchase volume, they are larger for transactors.

<a id='5cc725d8-dbfe-468d-b86b-9753a1375a20'></a>

## 3.2 Distribution of Credit Scores

To study the role of credit risk in credit card banking, we sort accounts by their FICO score at the time of account origination into 50 evenly spaced bins spanning 600 to 850. We use 600 as the lower cutoff because accounts with lower scores than this are rarely originated. FICO score is the industry standard credit score. It is intended to predict an account's credit risk relative to other accounts (though not its absolute level of risk, which depends on aggregate factors). In order to confirm that origination FICO score is a strong predictor of future charge-off rates in the cross-section of accounts, we estimate a series of regressions of charge-off rate using different sets of controls and fixed effects. The results,

<a id='ea7f235c-8cbf-4f80-9dff-71784b0cccc2'></a>

15

<a id='1bf42f99-b17b-4c29-9686-21d19f1f8d79'></a>

presented in Appendix Table C1, demonstrates that FICO score has significant predictive power for ex-post default rates. A basic model including only linear and quadratic FICO terms explains nearly 28% of the variation in charge-off rates. Introducing FICO bin fixed effects increases the R2 to 31%. Additionally, a substantial portion of charge-off variation is attributable to bank-specific factors, and accounting for these adds 18 percentage points to the explanatory power. Finally, interacting origination FICO with bank fixed effects further improves the predictive power, adding 24 percentage points and ultimately explaining 73% of the variation in charge-offs.

<a id='434de52b-8439-433a-ab77-0e5c5a98e2ca'></a>

Because of its informativeness about credit risk, banks use the FICO score to set accounts' borrowing terms. In particular, an account's origination FICO score strongly predicts its APR spread, which is set at origination and usually remains fixed for the account's life. This is due, at least in part, to the CARD Act, which prohibits banks from increasing an account's APR spread on outstanding borrowing. Appendix Table C2 shows that fixed effects for origination FICO-origination date and origination FICO-bank explain over 85% of the variation in the cross-section of APR spread. Thus, origination FICO is very informative about the cross-section of APR spreads. The following results further confirm this relationship.

<a id='8ab01be6-2639-4f1a-8078-f06b761729f5'></a>

We begin the analysis by examining the distribution of FICO scores across accounts.
Figure 1 plots the distribution of FICO scores across accounts. It plots the FICO share
of newly originated accounts (blue), all accounts (red), and the ADB-weighted share of all
accounts (green). The distributions of new and existing accounts are close to uniform for
FICO scores between 670 and 820, with a mode at 695.14 In contrast, the ADB-weighted
share is highest for FICO scores between 660 and 750.

<a id='6f8e3ca7-8b3c-484b-b06b-dbe3b1595a85'></a>

Within each FICO bin, we further sort the accounts into portfolios of borrowers and

<a id='195ad0ab-6e4c-4e3f-8a58-6803f190d2bf'></a>

14 The new and existing account distributions are nearly identical. This is because attrition rates are very similar for each origination FICO bin. Attrition rates are the share of accounts closed, which can occur due to to default, the customer voluntarily closing the account, the card getting lost or stolen, the customer dying, or other reasons.

<a id='15654094-1205-49dd-90f0-d8ce4f013168'></a>

16

<a id='42ef8c7a-d86d-4aaf-b71e-6eddc5992f82'></a>

transactors. This is important because borrowers and transactors have significantly different income and expenses streams. Figure 2a plots the share of borrowers across the FICO bins, on an equal weighted basis (blue) and weighted by balances (red). The share of borrowers is monotonically decreasing in FICO score. At 600 FICO, close to 80% of accounts are borrowers. This drops to 50% for 750 FICO, and decreases to a little less than 30% for FICO scores over 800 ("superprime"). Because borrowers have substantially higher balances than transactors, their balance-weighted share is substantially higher at all FICO scores. It is close to 100% for the lowest FICOs and remains around 90% for FICO scores of up to 750. It is worth noting that the balance-weighted borrower share remains above 50% for FICO scores above 800. Thus, lending to borrowers accounts for most of credit card banks' balance sheets.

<a id='52bab16f-c141-4efd-9e87-850621b95d0a'></a>

## 4 Decomposition of Income and Expense Streams

We analyze all major income and expense streams of accounts in the cross section of FICO scores. Importantly, we do so separately for borrowers and transactors, since these differ substantially across the two groups. We begin with the APRS charged by banks.

<a id='c56b030e-93a9-46c5-a80d-fe575a144fdf'></a>

## 4.1 APRs and Credit Losses

Figure 3 plots the effective interest rate (APR) paid by borrowers across FICO scores. We compute the effective APR from the reported interest payments and ADB and subtract the Fed funds rate to get the effective APR spread. The effective APR may differ from the reported APR because of promotions, during which a lower interest rate is charged (e.g., 0%). This is most common in the account's first year, but also occurs at other times. Using the effective APR accounts for the impact of promotions on banks interest income and consumers' cost of credit. We observe that a significant number of borrowers with high origination FICO scores take advantage of 0% APR offers to revolve credit. Notably, the

<a id='50db420a-0f95-47e0-9448-c205d2a60477'></a>

17

<a id='2b72284f-d466-47b5-a974-f44af12f2e9f'></a>

25th percentile of effective APR among borrowing accounts with an initial FICO score of 750 or higher is 0%.

<a id='48f24c8c-a189-49c9-b6b2-2adf8c27452e'></a>

It is important to note that almost all credit card APRs are a constant spread over the prime rate, which is itself a constant 3.0% spread over the Fed Funds rate. 15 Thus, it is natural to analyze APRs as a spread to the Fed Funds rate, which we call effective interest (APR) spread. These values across FICO bins are reported in Table 2, highlighting large APR spreads. The average APR spread across FICO scores is 14.5%, and even the smallest APR spread exceeds 7%. These spreads are much larger than those on other common types of bonds or loans. For instance, over 1997-2014 the average credit spread on investment-grade and high-yield corporate bonds was only 1.5% and 5.3%, respectively, and even the most distressed high-yield bonds, those rated CCC and below, had an average credit spread (11.1%) smaller than that of most credit cards.

<a id='0e64b332-b7db-4dc4-b60f-e6fec9bdaaaf'></a>

Since credit card lending is unsecured lending to consumers, it is exposed to a significant risk of credit losses. Hence, we first analyze whether the APR spreads are explained by similarly large credit losses.

<a id='580a9dfd-a359-472b-a44a-2d3606c25d0c'></a>

Figure 4 is a stacked plot comparing the interest income (blue) of borrower accounts in the FICO bins against their credit losses (green) and interest expenses (red). These quantities are plotted on the left axis. Income is plotted as a positive quantity, while losses and expenses are negative. We focus on borrowers since transactors do not have interest income or credit losses.

<a id='7008c52c-15b4-47b2-99fb-234132516ff8'></a>

The (net) credit loss rate measures the quantity of charge-offs per dollar of lending per year over our sample. We net charge-offs against any recoveries, which for credit card lending are small. Interest income is just the interest paid by the accounts. Hence, the plotted rate is exactly the average effective APR rate in Figure 3. We assume the interest rate paid on

¹⁵As of 2022, 98 percent of general purpose accounts in the Y-14 were variable rate cards according to Consumer Financial Protection Bureau (2023). In a highly-cited paper, Ausubel (1991) documented that during the 1980s credit card APRs had low sensitivity to the Fed funds rate. This has not been true for a long time, as credit card APRS have moved closely with the Fed funds rate since at least 1995.

<a id='4c699dad-0fd2-4c77-9667-a3f9e91b9712'></a>

18

<a id='e8d89622-7c48-4d9d-a0ac-2120bcaf442f'></a>

financing equals the Fed Funds rate. 16 Thus, the difference between the interest income and expense rates equals the effective APR spread reported in Table 2. In analogy to bonds, we can also view it as the credit spread on these accounts.

<a id='32ef460d-471f-40a3-8be2-4ba684bf0cd4'></a>

Since our goal is to understand the profitability of accounts over their lifetime, we plot the annual average rates of these quantities from the time of origination until the end of the sample. To calculate the lifetime average rates for each origination FICO bin, we divide the cumulative monthly dollar amount of the quantity of interest (e.g., net charge-offs) for all accounts in the FICO bin over the sample period by their cumulative monthly balances over the same period. This ratio gives the rate of the given quantity per dollar of monthly balance. To annualize it, we multiply it by 12. To combine the cohorts (origination months) of a FICO score bin, we effectively treat them as one large portfolio and sum the numerator (e.g., net charge-offs over the sample) for all the cohorts of the FICO bin and divide by the sum of their balances. We follow this same approach for all the quantities plotted in the figures below.

<a id='773f9ce8-34c1-4c2d-8f52-9df46a2480ec'></a>

Figure 4 confirms that lifetime credit losses are substantial for many FICO scores. Moreover, they are strongly, nearly linearly, decreasing in FICO score. At the lowest origination FICO score (600), lifetime net credit losses are a very high 9.3% of balances per year. By 720 this decreases to a still large 5.7% of balances per year over the lifetime, which is also the loss rate for credit card lending in the aggregate in the sample. Even at 800 origination FICO ("super-prime" according to Experian), the credit loss rate is still 3.2%. By 850 FICO, the highest possible, the credit loss rate drops to 1.3% per year. Note that these FICO scores are the accounts' score at the time of *origination*, not at the time of default. By the time an account defaults, its FICO score has usually deteriorated substantially. However, we

<a id='63a50fda-0b70-48bf-b15e-2f9f695921ba'></a>

16 There are two main reasons why we believe this is appropriate. First, the interest expense rates of banks that engage mainly in credit card lending, such as American Express, Discover, or Synchrony bank, is very close to the Fed Funds rate. The reason is that they lack a deposit franchise and hence fund themselves mostly by selling short-term CDs at competitive rates, i.e., close to the Fed Funds rate. Second, for banks that do have a deposit franchise, and hence obtain deposit financing at lower rates, the difference should be viewed as a payoff to their deposit-taking business, which involves is its own substantial costs, not their credit card business. Thus, to be conservative we set the interest expense rates to the Fed Funds rate.

<a id='3729be95-4a8e-4140-b273-a0943a65c8bf'></a>

19

<a id='19abb54f-96c7-4c26-9b6b-dd58f36352aa'></a>

need to map accounts' credit losses to their origination FICO scores in order to compare them with their APR spreads, which are fixed at origination. In addition to default-related charge-offs, there are also charge-offs due to fraud. The cost of these is 0.18% of ADB per year, so far smaller than credit-related charge-offs.

<a id='aa011e38-1851-4b09-b96d-8136ebde1d82'></a>

To test whether APR spreads are just compensation for average default losses, we subtract the credit loss rate for each FICO bin from its effective APR spread. We refer to this as the "default-adjusted credit spread" and plot it on the right axis (black line) in Figure 4.

<a id='3e4db06e-44a2-4065-86e1-86d05de10c4a'></a>

We find that, despite the high credit loss rates, the default-adjusted credit spreads are positive and large. Thus, credit card borrowers pay rates that are a large spread over expected default losses. Indeed, the average defaulted-adjusted credit spread (balance-weighted) is a very large 8.8% APR.

<a id='118ad03d-b7b9-45c8-ab26-34782e4533a2'></a>

Figure 4 further shows that the default-adjusted credit spread is strongly decreasing in FICO score. It is close to 12% for FICOs below 660. There is a jump down to 10% between 660 and 670 FICO, likely related to this being the cutoff between non-prime and prime borrowers. The default-adjusted credit spread then decreases nearly linearly from around 10% at 670 FICO to 6% at 850 FICO.

<a id='1e202e70-ee6d-4630-afd6-2e1f4ff09368'></a>

Thus, although all borrowers pay a credit spread, this is much larger than their expected credit loss, the gap is much wider for lower FICO score borrowers. This suggests that credit card rates may price in a large credit risk premium, and that the risk premium decreases in borrowers' FICO score. We investigate this hypothesis in section 5.

<a id='ce8cdcfc-a2a0-4fcc-ba47-cb1066dc54c2'></a>

Next, we analyze accounts' non-interest income and expense streams. We incorporate them into the calculation of returns on the FICO bins and ask to what extent they help explain the large default-adjusted credit spreads we find in Figure 4. We also analyze the returns banks earn on transactors, which are exclusively from non-interest sources.

<a id='1815674e-f2c6-4806-bbed-f55f6847ad92'></a>

20

<a id='cfb9c414-82f2-4382-ba42-02c611a8f847'></a>

## 4.2 Non-interest Income and Expenses
The main non-interest components of credit card business' profits are interchange income, rewards expense, fees, and operating expenses.

<a id='987c8383-1948-4e77-947f-fa7759f6d9f9'></a>

### 4.2.1 Interchange and Rewards

When a credit card is used to make a purchase, the merchant pays a "processing fee" or "swipe fee", which is split between the bank that issued the credit card, the credit card network (Visa, Mastercard, American Express, or Discover), and the "payment processor".

In the US in 2023, these three components of credit card processing fees amounted to $162.5 billion (CMSPI, 2024). The bulk went to interchange fees, the component received by the card-issuing bank. In our data, we find that interchange fees average 1.82% of the purchase price. On top of this is the network fee, which is paid to the credit card network, and is between 10-20 basis points of the purchase price for Visa and Mastercard (CMSPI, 2024).17

<a id='f5663ea3-9c70-4350-88ed-0a62ffa16dae'></a>

A striking feature of credit cards is the prominence of rewards payments. Rewards are paid to the cardholder by their bank in return for using the card. Like interchange, they are also a percentage of the purchase price. Rewards are paid as cash, airline miles, or points that can be redeemed for cash or travel.

<a id='d6d051c0-d557-41d6-9905-8c5cf6822c20'></a>

Rewards and interchange are closely intertwined. Rewards expenses are covered by banks' interchange income, which is why bank filings usually report the net of the interchange income and rewards expenses as a single value. We find that banks' rewards costs are on average 1.57% of purchase volume. Hence, on average, banks pass on 86% of their interchange income as rewards to card users.

<a id='8486ca41-0a0b-4146-aafe-0b661e8279dd'></a>

17 The total interchange and network fee charged on Visa cards is between 1.51% and 2.5% of the transaction value, plus $0.10 per transaction for transactions that take place in person. (https://www.clearlypayments.com/interchange-rates-in-usa/). For "card not present" (i.e., online) transactions, rates are higher, between 1.89% and 2.5% of the transaction value, plus $0.10 per transaction. Mastercard's fees are similar.

<a id='5baf422f-7a7b-4fc0-b436-06b1aaf60889'></a>

21

<a id='fceccc43-9d5c-41b7-8cfb-e685d6b86a7d'></a>

We compute the interchange and reward rates from the Y-14's portfolio-level data rather than the account-level data. The portfolio data reports the dollar amounts of interchange income and rewards for each bank in each month. We calculate bank-level purchase volume by aggregating the purchase volume of the individual accounts during the month. We then compute the interchange and reward rates by dividing the dollar value of interchange/rewards for the bank by the bank's purchase volume. 18 Appendix A.1 provides a detailed description of how we compute both rates.

<a id='ceff1929-a111-4f48-963d-ce9787272846'></a>

Since interchange and rewards are proportional to purchase volume, we first examine the cross-section of purchase volumes by FICO score. We separate borrowers and transactors since we are interested in measuring banks' return on assets for each group. Since transactors do not pay interest, the return banks make on them depends much more on net interchange income.

<a id='f993ab6d-7f1d-4ff8-b21c-d16f0111f322'></a>

Figure 5 plots the average purchase volume for borrowers and transactors within each origination FICO bin. We average only active accounts, that is, those that have some purchase volume, payment activity, or balance that month. By construction this includes all borrowers, but excludes transactors that show no activity at all. These inactive accounts do not use up any of the bank's balance sheet, because it does not provide them with any financing. 19 At the same time, there is little to no cost to the consumer of keeping an inactive account open, as long as it does not have an annual fee. We find that 22.6% of all accounts in our sample are inactive in a given month. Of the active accounts, 57.1% are borrowers and 42.9% are transactors on average.

<a id='77c85ed7-a94a-4957-93a9-79d07f3fecc3'></a>

Figure 5 reveals two main patterns. The first is that average purchase volumes are higher

18 The account-level data does contain a running sum of unspent rewards. In principle, this could be used to estimate account-level reward rates. However, there are significant limitations to the account-level data. The data does not record how much rewards were spent during month, so one cannot separate new rewards from rewards spent. Also, many account-level rewards entries are missing and, when recorded, are noisy. For these reasons, and to ensure that rewards aggregate correctly, we use the portfolio data.

<a id='e9a48c1f-6519-445e-b64c-b4ff16d6e840'></a>

19Excluding inactive accounts does not impact our analysis since they do not affect the balance sheet. We exclude them because we are interested in analyzing the average purchase volume of cards that are actually used. Inactive accounts may impose some administrative costs on the bank. These are included in operating costs, which we amortize over all active accounts.

<a id='5bb0e37a-80f7-4d74-8831-46d9cdbeeea0'></a>

22

<a id='6788e745-bf24-4a3f-b4d1-ecbad7ddbd62'></a>

for active transactors than for borrowers across all FICO scores. This is not surprising, since by construction transactor accounts have no debt, and hence are likely to have more capacity to spend.

<a id='7c489c8c-8e36-4bca-800d-3ea3476391e2'></a>

The second pattern is that the average purchase volume increases in FICO score for both transactors and borrowers. For transactors, purchase volume rises from a little over $600 per month for 600 FICO to about $1200 for 720 FICO, and is around $1600 per month for FICO of 770 and above. For borrowers, purchase volume averages $200 for 600 FICO, rising to $600 for 720 FICO, and reaching around $1300 by 850 FICO. This is not surprising either, because an account holders' FICO scores and incomes are strongly positively related, hence accounts with higher FICO scores tend to have more spending power.

<a id='f28a2544-e5fd-4089-a874-8968ffc49992'></a>

To understand how interchange and rewards contribute to the overall profitability of credit card portfolios, we compute lifetime interchange and reward as a fraction of ADB following the same procedure as above for interest income and credit losses. Figure 6 plots the cross-section of these rates. As above, the rates are annualized. Unlike interest income and charge-offs, interchange fees and reward expenses apply to both transactors and borrowers, and we plot them separately.

<a id='19d3ce65-2249-47af-b839-6397fcc0bdd3'></a>

Figure 6a plots the results for transactors. Note that interchange and rewards are plotted on the left axis, while the difference between them, net interchange, is plotted on the right. As the figure shows, for transactors, the interchange income (yellow) is close to 44% of ADB on an annualized basis for FICO scores between 600 and 800. Above 800 the average drops to around 33%. Rewards expenses (purple) are about 40-30% from 600 to 800 FICO.

<a id='0bf26659-bcbd-4419-8304-5df4ad678621'></a>

This means that the interchange income generated by transactors for the bank is akin
to it charging a 38% interest rate on the funds it (implicitly) provides them, though the
payment is made by merchants, not the cardholders. This is a very high rate. To understand
how it arises, recall that the average interchange rate is about 1.82% of purchase volume.
This means it is over 2% of ADB, which is the average balance during the month and hence
is less than purchase volume as long as the purchases are not all at the beginning of the

<a id='6e81657e-4a8c-4e80-8bd4-dbc1f0d675ac'></a>

23

<a id='6b9e8fa9-cbff-4887-b3ef-8883b9fbc450'></a>

month. Annualizing this figure (by multiplying by 12) gives the average annual rate of 38%. Similar calculations explain why the annual reward expense rate is 24.6% of ADB on average.

<a id='eb0007c3-a7b6-40fa-9131-6f90b1edc7b8'></a>

While a majority of interchange income is passed through to cardholders as rewards payments, net interchange income is substantial for transactors. Figure 6a shows that between 640 FICO and 810 FICO the average net interchange rate is about 4.6% of ADB annually. Thus, due to interchange banks earn an annual rate of about 4.6% per dollar of financing they provide to transactors for purchases.

<a id='4cabbb1c-a5f4-4718-89f1-a0482f633e9d'></a>

For borrowers, interchange and rewards rates per dollar of ADB are much lower than for transactors. Figure 6b shows that average annual interchange income per dollar of ADB is flat at around 2.6% for FICO scores below 740, and then increases monotonically to 7.5% by 850 FICO. This increase is mainly due to a higher ratio of purchase volume to ADB for the high-FICO accounts. There is a similar pattern for rewards expenses: they are about 2% for FICO scores below 700, then rise to 7.4% by 850 FICO.

<a id='097a195d-c47b-4e2b-a434-8320e5d15e89'></a>

Net interchange income annually per dollar of ADB (right axis) is also much smaller for borrowers. It is uniformly less than or equal to 0.8% per year, and is between 0.35% and 0.6% for FICO between 620 and 815. For the highest FICO scores net interchange falls below 0.2%. The decrease is due to premium credit cards paying higher rewards rates. Such premium cards are mainly held by higher income, and thus higher FICO score, cardholders.

<a id='59998705-447f-475b-84ef-7bd2ec97b5b8'></a>

Thus, Figure 6 shows the net interchange income earned from transactors is large relative to assets. As we show below, it accounts for the bulk of the return on assets from transactors. In contrast, for borrowers it is a marginal component of return on assets compared to the magnitudes of interest income and credit spreads. Nevertheless, net interchange is positive for borrowers. Thus, rewards do not explain credit cards' high APRs; to the contrary, since net interchange is positive, it adds to the large default-adjusted credit spreads, and deepens the puzzle of why credit card APRs are so high.

<a id='fd21deeb-ac38-4d5a-a1e9-30b36161b49f'></a>

24

<a id='2da529bf-8a84-47b5-8b69-2ef86d5bd007'></a>

4.2.2 Fees

Credit card lending also generates other fee income besides interchange fee, including annual fees, late fees, balance transfer fees, over-limit fees, cash advance fees, convenience fees, and insufficient funds fees. During our sample period, such fees average 2.6% of credit card balances, accounting for approximately 10% of total credit card lending revenue.

<a id='d95e1f06-0200-4279-82e7-f40a41cc1434'></a>

The largest categories are late fees, annual fees, and balance transfer fees. Appendix Figure B1a plots average non-interest fees by FICO bin as a share of ADB during the life cycle of an account, starting from account origination. Fee income is seasonal, peaking every 12 months when annual fees are charged. Annual fees are highest for accounts in the highest and lowest initial FICO bins. At both extremes they are above 1% of ADB in the first few years.

<a id='d8e0f130-7c29-4d8f-9000-c1e7412b2e8f'></a>

Another significant source of fees is balance transfer fees, which accounts pay in order to transfer their borrowing from another credit card. These fees are highest for the lowest FICO accounts. Specifically, the 600 and 650 FICO accounts pay an annualized 6% and 2% of ADB, respectively, as a transfer fee in the first month following origination.
Table 2 reports income from fees as a percentage of ADB across FICO bins for borrowers

<a id='351e80fe-37d4-4409-8992-13eeb566db68'></a>

(panel A), and transactors (panel B). For borrowers, fee income is highest for subprime FICO scores (660 and below), driven by balance transfer fees and late penalties. Accounts with 600 FICO score pay almost 5% in fees on average, and even those with 640 FICOs pay nearly 3.7%. For FICO scores between 680 and 800, fee income is flat at around 2%. Above 800 FICO score fees rise again, to nearly 2.9% for 850 FICO score, driven by the higher annual fees charged by premium cards, which are more common in this FICO range. The overall ADB-weighted average fee income for borrowers is 2.29% of ADB.

<a id='4727fcb1-94d1-41ca-a177-4c23d8f1b986'></a>

Fee income as a share of balances is high for transactors. Subprime accounts again generate the highest fees as a share of ADB, with fee income of 6.6% to 14.1% of ADB. The high rate is due to annual fees and the relatively low ADB of these accounts (not to

<a id='233d621a-4c72-4f72-9b0d-ad97629dece2'></a>

25

<a id='70b2eeeb-3017-4848-b228-353a97a8baf1'></a>

balance transfer or late fees, since transactors do not incur these fees by construction). For FICO scores of 680 and above, fee income is flat at around 4-5%. The overall ADB-weighted average fee income for transactors is 4.96%.

<a id='67e725bc-0ccc-47ac-9fa2-dce6cc16e2e4'></a>

Adding interchange and fee income and subtracting reward expenses gives net non-
interest income. Net non-interest income as a fraction of ADB is substantial for borrowers
and very large for transactors: for borrowers the ADB-weighted average is 2.7% of ADB,
for transactors it is 9.6% of ADB. Since transactors do not pay interest, this is all of the
income earned from them.

<a id='717dff0d-18a1-4cdc-9aa8-8e754e8d6686'></a>

Adding the non-interest income to the default-adjusted credit spread, we get the gross lending margin, the return lenders earn from borrowers after accounting for all marginal income and expenses, but not operating expenses. We find that credit card lenders earn a very large 11.5% average gross margin on borrowers. Figure B2a plots the cross-section of gross margin by FICO bin. Like its components, it is decreasing in FICO score, from about 17.5% for a 620 FICO score to 9% at 850 FICO. Thus, it shows that the gross lending margin is large for all FICO scores-even the very safest borrowers generate a 9% gross lending margin. At the same time, the gross lending margin varies substantially across FICO score, with higher-risk borrowers corresponding to much larger gross margins.

<a id='b2bdf555-f229-4df3-8828-1d46323cfdb8'></a>

## 4.3 Operating Expenses

Banks are not merely portfolios of financial assets and liabilities; to a large extent, they are retail businesses. Credit card lenders exemplify this retail-facing aspect of banking as they engage in extensive consumer interaction. From customer acquisition and applicant screening, to card administration and customer service, these activities incur large operating expenses.

<a id='9dcc7787-fb9e-4f8c-bdbd-f7f3db2f9884'></a>

To illustrate this, we examine the operating expenses of Capital One Bank. Capital One is arguably the bank most specialized in lending to general purpose credit cards. It was

<a id='2550760c-4ff5-4bfe-b46f-fd30cd8e1a41'></a>

26

<a id='444ce38d-d1f0-4e84-ac88-d74d2fce3dff'></a>

founded as a credit card lender and is today the third largest credit card lender, following JP Morgan and Citibank, which have far larger overall balance sheets. Figure B3 in the Appendix present excerpts from Capital One's 2023 annual report that detail the compo-nents of its operating expenses for the whole bank, and for just its credit card operations. In addition to its credit card operations, Capital One maintains a substantial deposit fran-chise, accounted for mainly under its "Consumer Banking" segment, and provides lending and other services to firms under its "Commercial Banking" segment.

<a id='f100c927-6475-462d-8b36-5fd681a627fd'></a>

Appendix Figure B3a shows that salaries and marketing are the largest components of operating expenses. Other major costs are for occupancy, and for communications and data processing. In 2023, Capital One held an average of $141 billion in credit card loans, which represented 45% of its loan portfolio and 30% of its total assets (it also had significant securities holdings). As Appendix Figure B3a shows, the bank's overall operating expenses, including marketing, totaled $20.3 billion. It attributed $12.5 billion to its credit card operations, shown in Appendix Figure B3b as the "non-interest expense" of its credit card segment. 20

<a id='a4548b9c-cf2b-4ac9-9944-4acbb879349b'></a>

These figures show that the credit card segment incurs a disproportionate fraction of the operating expenses (including marketing) compared to its share of assets. The credit card segment represents 30% of Capital One's assets but constitutes 61.6% of its operating expenses.

<a id='1bdbd7e3-3104-49aa-9744-4e6c151db275'></a>

Another interesting comparison is with Capital One's Commercial Banking segment. It had an average of $92.5 billion of loans (65% of the magnitude for credit card loans) and was attributed $2.0 billion of non-interest expense (16% of the magnitude of credit loans). If its operating expenses had scaled proportionately with its loan book, the operating expenses of commercial banking would have been $8.2 billion instead. For comparison, the pre-tax net income of the commercial banking segment was only $0.9B. This comparison illustrates

$^{20}$The $20.3 billion is also listed as "non-interest expense" in Appendix Figure B3a. Adding up the non-interest expense for each of the three business segments confirms that they sum up to $20.3 billion.

<a id='c3ce7f17-a7e2-4d26-8c7d-4d8e7dd852d5'></a>

27

<a id='993ef890-42fa-4a0b-a20c-9b78d5cca365'></a>

how much greater are the non-financial costs involved in operating and marketing the credit card business, which is highly retail-facing, than the commercial banking business, which is not.

<a id='48af2ea5-289e-4f09-8be6-87a1e984e39c'></a>

Another way to assess the operating expenses is as a share of assets. For Capital One's Credit Card segment, operating expenses are 8.8%. This means Capital One has to make 8.8% on every dollar of ADB just to recoup its operating costs. This is a very large amount. To put this into perspective, the operating expenses to assets ratio for the aggregate US commercial bank system in 2023 was 2.2%. This was also very close to the ratios for JP Morgan, Bank of America, and Citigroup. Thus, Capital One's credit card segment was four times as costly to operate as the average bank asset.

<a id='fb131c93-7589-409d-a9fd-115d6be69c90'></a>

We find consistent results using Y-14 data, which contains information on operating expenses for the specific credit card segment reported by banks. The Y-14 operating expense includes spending on servicing, billing, card issuing, and authorizations. It does not include the costs of debt collections, fraud, and interchange processing, which are recorded separately. It does include spending on marketing, which is very substantial, and which we discuss in more detail below. We find that operating expenses are large. In the Y-14 data they average 4.76% of balances for our sample, as shown in Panel C of Table 2. Thus, operating costs offset a substantial part of the gross margin.

<a id='6e7c84c7-fc05-4e77-97ce-1915dfa38ee3'></a>

Drechsler, Savov and Schnabl (2021a) show that banks pay significant fixed operating costs to gain market power in the retail deposit market. This enables them to borrow at rates that are both below market rates, and are relatively insensitive to market fluctuations.
Since credit card banking is highly retail in nature, the same mechanism is likely at work here. That is, credit card banks spend so much on fixed operating expenses because it gives them substantial pricing power, i.e., a credit card franchise. This would help explain their large default-adjusted spreads and gross lending margins.

<a id='07b63d5f-4a36-4cd0-9550-00413b3d6ae4'></a>

One way to examine this hypothesis is to look at credit card banks' spending on market-
ing. The role of marketing is to generate additional demand for a product without changing

<a id='1587f5a0-fa70-4f9f-8941-94adf4fbfb52'></a>

28

<a id='a3ccff5c-f00e-41e0-9d2b-40fcad04d1f7'></a>

the product itself. If the firm has pricing power, this additional demand generates additional profit by increasing the markup the firm can charge for a given level of supply.

<a id='d3ed521e-2c37-4243-a8d5-5d2f32847ead'></a>

Therefore, if we observe large spending on marketing, this implies that marketing is effective (or perceived as such) at increasing demand for the product, and hence at increasing the price the firm can charge for a given supply. For credit cards, this price is the APR spread, fees, or interchange rate that banks can charge.

<a id='2e53f99e-2246-4cf0-89c9-c667043856ce'></a>

We find that marketing is one of the largest components of operating expenses for credit card lenders, and that credit card banks are some of the biggest marketers in the US. For instance, in 2023, Capital One spent $4 billion on marketing, and American Express spent $5.5 billion, making them the sixth and seventh largest advertisers in the US in 2022 (Statista). Their marketing expenses matched those of international consumer product giants Nike ($4 billion) and Coca-Cola ($5 billion). They were also large compared to the largest banks: Bank of America, the second-largest US bank, had 6.7 times the assets of Capital One in 2023, but spent less than half ($1.9 billion) on marketing, while JP Morgan, the largest US bank, with 8 times the assets of Capital One, spent about the same ($4.5 billion).

<a id='79b319ca-36ae-4f49-9276-e94ab44bd616'></a>

More generally, using Call Reports, we compare the marketing expenses of banks that have a relatively high share of loans in credit card lending, which we classify as "credit card banks," to all other commercial banks. Appendix Figure B4 plots the result. Credit card banks spend between 1-2% of their assets annually on marketing, compared to less than 0.1% for all other banks. Even this estimate for credit card banks is a lower bound, since banks that meet the classification for this still include significant shares of non-credit card assets, as in the case for Capital One. If we were able to isolate the marketing expenses attributable specifically to the credit card business, their share of assets would be even higher.

<a id='8d210baa-4f20-483e-9156-5e0218a4d626'></a>

The fact that marketing's share of assets is more than ten times higher for the credit
card business is consistent with it being a highly retail, consumer-oriented business, making

<a id='5aafd8df-6440-419c-8c72-64a565ecdee4'></a>

29

<a id='15ea0e3b-12c7-4590-94c8-8253cf84c3d1'></a>

marketing an effective channel for generating demand and thus increasing pricing power.
Next, we examine how credit card banks' operating expenses relate to their ability to generate additional income using Y-14 data. Figure 7 shows a positive relationship between banks' interest spreads (or gross margins) and their operating expenses (as a share of ADB) separately for different levels origination FICO.21 The bubble size represents the size of credit card lending. The figure suggests that controlling for the same ex-ante riskiness (within the same FICO bin), banks with higher operating expenses tend to charge higher interest spreads (Panel A) and achieve greater gross margins (Panel B), particularly among those with large credit card operations.

<a id='196abe13-8497-45ed-844e-b442a8d0a5d4'></a>

We analyze this relationship formally by estimating the following weighted cross-sectional
regressions:

<a id='92667030-3172-4786-befc-cdc26c6a2f39'></a>

Y_{b,f} = \alpha + \beta Operating Expense_b + \delta_f + \epsilon_{b,f}

<a id='bffe32b3-48e5-4957-b5af-2f1497cee1f5'></a>

where the outcome variable, Y_b,f, represents lifetime borrower interest spread, net charge-off rate, or gross margin, which are aggregated from all observations within a bank (_b_)-origination FICO bin (_f_) level. Operating expense_b is the bank-level average operating expense rate from the Y-14 portfolio-level data. We include origination FICO bin fixed effects, denoted by δ_f, to control for the ex-ante credit risk. Standard errors are clustered at the bank level.

<a id='db0c74a0-a439-481a-b02b-4b00761abdb6'></a>

Consistent with our hypothesis, column (1) in Table 3 shows that, within a credit card portfolio of the same credit risk, higher operating expenses are associated with higher interest spreads. In terms of economic magnitudes, a 1% increase in a bank's operating expense rate corresponds to a 62 basis point increase in the interest spread charged to borrowers. In column (2), we find no significant relationship between operating expenses and ex-post default rate when controlling for ex-ante credit scores, suggesting that higher expenses do not affect borrower selection based on unobservable credit characteristics at the same credit

²¹We focus on origination FICO bins of 650, 700 and 750, where most borrowers are concentrated.

<a id='f7ba25b4-837a-49bf-bd69-7fce90f11047'></a>

30

<a id='9c12c8e5-c53b-4f23-8924-e7558215d7ad'></a>

score.

<a id='64193a34-16bb-455f-a0a2-066c79beea45'></a>

It is also important to note that the core business of credit card banks for borrowers is revolving credit rather than transaction-based services. As we showed, borrowers generate lower purchase volumes compared to transactors, which may reduce the need for extensive customer service. To the extent that operating expense rate is similar across both borrowers and transactors, higher operating expenses provide credit card banks with greater pricing power, allowing them to charge borrowers higher interest spreads.

<a id='b8d88999-8a48-4531-9aef-f407d0c2e472'></a>

Finally, column (3) shows that a 1% increase in the operating expense rate is associated with a 1.2% rise in gross margin, consistent with banks incurring higher operating expenses to attain greater pricing power.

<a id='6aeee53d-ca3c-47d2-a6b0-64c834809d4e'></a>

Accounting for operating expenses, we have now covered all of the main components of
credit card banks' income and expenses. In the next section, we combine these to calculate
their return on assets for each FICO bin.

<a id='bcd2b361-f68c-497d-ab2d-081e5d3a7a70'></a>

## 4.4 Putting all Together: Return on Assets

Adding together all of an account's streams of income and expenses per dollar of ADB, over its lifetime, gives us the banks' return on assets (ROA) for the account. Specifically, ROA equals interest spread minus net charge-offs (default-adjusted credit spread), plus net interchange income (interchange minus rewards), plus the fee income rate, minus the operating expense rate. The last column of Table 2 reports the ROA across FICO bin and borrower/transactor group.

<a id='c2f4cd9b-6528-4b89-93f7-cc079db57de2'></a>

Figure 8 (right axis) displays the ROA for borrowers with different FICO scores at origination, as a percentage of lifetime ADB. ROA is high and increases significantly with ex-ante credit risk, rising from 5% for borrowers with an initial FICO of 800 to 9% at 660 and reaching 11% at 625. The magnitude of the increase in ROA in default risk is similar to the one we found for default-adjusted APR.

<a id='b7d56a3d-060f-48fe-98e6-8b2f8770ef25'></a>

31

<a id='2740235c-57fb-4fbc-8c3b-357cd1432351'></a>

For transactors, ROA remains flat at 2.8% between FICO scores of 680 and 820 (Figure B6 in the appendix). The lower ROA observed at higher FICO scores is driven by higher rewards costs, while the higher ROA among riskier subprime borrowers is largely due to shorter and fewer transacting periods, leading to lower ADB. Notably, the ROA on transactors is slightly lower than that of even the safest borrowers and remains independent of ex-ante credit risk. This is expected, as transactors, by definition, carry no credit risk. Both the fact that transactor ROA is flat across FICO scores, while borrower ROA is steeply increasing in credit risk, suggest that credit card pricing incorporates a substantial component that is driven by risk.

<a id='9a639314-a9e4-430d-ba28-c63258a7149f'></a>

The high ROA of credit card lending is reflected in the aggregate ROA of banks specializing in this sector. 22 Appendix Figure B7 presents a time series of ROA for credit card banks and other commercial banks based on Call Report data since 2001.23 Call Reports allow us to extend the analysis further back in time to observe the performance of credit card lenders during the Great Financial Crisis (GFC). We compute ROA in the same way as account-level credit card net margin, except that we substitute "provision for credit losses" in place of actual charge-offs, to match the timing of net income. Over the past 25 years, credit card banks have maintained an ROA around 4%, roughly three times higher than that of non-specialized banks. For comparison, we also include the ROA of general-purpose credit card loan portfolios from Y-14M data, which is available since 2015. ROA derived from the Call Reports co-moves strongly with the time-series ROA calculated from Y-14 portfolio-level data when the sample periods overlap. However, bank-level ROA is lower than the net margin of credit card portfolios, as credit card banks also operate other, lower-return business segments. During the GFC, credit card banks' ROA declines sharply,

<a id='77d3c48c-451b-4f4b-be63-b7cadead3f57'></a>

22 According to the FDIC Quarterly Report for 2024:Q2, the average ROA for credit card banks is 3.18% (ROE of 31.03%), compared to an average ROA of 1.2% (ROE of 12.26%) for commercial banks.
23 We define credit card banks following the Federal Reserve's Report to the Congress on the Profitability of Credit Card Operations of Depository Institutions", which classifies credit card banks as those where: (1) more than 50% of total assets are loans to individuals, and (2) at least 90% of consumer lending is related to credit cards or similar plans.

<a id='211f0c5f-c55e-4eed-be3d-29d3496c293b'></a>

32

<a id='5fb1a77d-e9a0-48a5-af76-68f358e63b36'></a>

dropping to approximately zero in 2008 due to high credit losses. This is the only period in the sample where credit card bank profitability turned negative, as the large loss provisions during COVID-19 did not materialize and were quickly reversed. Despite the losses, credit card banks' ROA is higher than that of other banks in 2008, due to the substantial spread priced into credit card lending. Thus, the spread (i.e., risk premium) is large enough to absorb most of the increase in credit losses, even during the 2008 crisis.

<a id='f681671e-ee7e-45a2-b9ce-0a0573f7e926'></a>

# 5 Credit Card Risk Premium

As was shown in the previous section, the ROA of the credit card portfolios is closely linked to the default risk of their borrowers, as accounts with lower FICO scores (higher default risk) have substantially higher ROA. This suggests that the high return to credit card lending is in part due to a default risk premium. Moreover, if credit card charge-offs tend to be particularly high during economic downturns and periods of heightened financial stress, banks may require higher compensation for bearing this risk. This raises the question of whether the risk premium on credit card lending is consistent with those observed in other assets that earn a compensation for exposure defaults during economic downturns.

<a id='b83bf51e-3060-4325-90eb-8ef026795c98'></a>

Figure 9 illustrates the time series of charge-off rates across various types of loans and corporate bonds. Panel (a) shows that credit card charge-offs strongly correlate with default rates on other loan types, especially during recessions. Notably, credit card charge-off rates are the highest and most sensitive to the default cycles. The commonality in defaults, and the fact that the common component spikes in recessions, suggests that this common default risk is undiversifiable (i.e., systematic) across loan markets, and may be priced. Panel (b) focuses on the relationship between speculative-grade corporate bond defaults and credit card charge-offs. The series exhibit strong co-movement and comparable default rates.²⁴

²⁴However, corporate bonds maintain a higher recovery rate of around 40%, compared to the much lower 15% for credit card charge-offs.

<a id='67e30c03-7b9e-4993-81e9-671f4e43ae0e'></a>

33

<a id='aee25e8e-3efb-49fc-87fc-09bebf536634'></a>

This comparison suggests that corporate bonds can serve as a benchmark for assessing the risk premium in credit card lending. Corporate bonds are an especially useful benchmark because they are are traded in secondary markets, and are very large. Indeed, the corporate bond market is the main market for pricing credit risk.

<a id='13793739-94d1-479a-ac31-b26d0459fbbc'></a>

We have seen that sorting on origination FICO score corresponds to large cross-sectional differences in average default rates across credit card loans. Figure 10 shows that it also corresponds to large differences in the volatility of charge-offs over time. Panel (a) plots the time series of charge-off rates over the life cycle for different origination FICO portfolios from the 2016 cohort. The average level of charge-offs is decreasing in origination FICO score, as one would expect. The charge-off levels are also quite stable over the life cycle, though the onset of the covid period confounds the time series around the 4-year (48 month) mark. As shown in Zhou (2025), the disbursement of covid checks caused a large decline in charge-offs, especially among the low-FICO accounts that account for most charge-offs.

<a id='f8a1f7e9-fdba-4405-97c5-a14bfacac0ce'></a>

The other stand-out characteristic of the life cycle of charge-off rates is that they spike early in the life cycle for all FICO scores. The spikes correspond to the time when the promotional APR period expires, at which point borrowers must begin paying their regular APR rate.

<a id='4ee9b452-5bf8-4d83-99bc-2cda546d8ed5'></a>

Panel (b) of Figure 10 shows the time series evolution of credit card charge-offs across origination FICO scores. Charge-offs are highly correlated across FICO portfolios, rising and falling in tandem with the aggregate charge-off rate. This shows that there credit card charge-offs contain a common, undiversifiable component. In addition, the figure indicates that lower FICO score accounts experience a steeper increase in charge-off rates when the aggregate charge-off rate increases. Hence, the lower the FICO score, the greater is an account's sensitivity to aggregate charge-off risk.

<a id='26e90a0e-de9a-49ef-86ac-a6b0141613c5'></a>

To quantify the exposure of each FICO score portfolio to this aggregate charge-off risk,
we follow the standard two-stage approach of Fama and MacBeth (1973). We first estimate
a single-factor model of default risk using the cross-section of FICO portfolios. We proxy for

<a id='54c477bb-51aa-498f-bc26-c11f2e7d7a9b'></a>

34

<a id='e30de406-6d0c-47c3-aebd-524c39401fb7'></a>

this factor, the systematic component of charge-offs, with the monthly change in the charge-off rate on the aggregate credit card portfolio. We then estimate the beta of each FICO portfolio to systematic charge-off risk by regressing the monthly change in its charge-off rate on the factor:

$\Delta$Charge-off Rate$_{i,t}$ = $\alpha_i$ + $\beta_i\Delta$Charge-off Rate$_t$ + $\epsilon_{i,t}$. (1)

<a id='b4de2ee9-dd1d-4e9d-ba55-e34c6686a978'></a>

Figure 11 plots the estimated betas of the FICO portfolios against their corresponding charge-off rate. The estimates reveal a strong factor structure in the charge-off risks of the FICO portfolios, with charge-off beta strongly and linearly decreasing in FICO score. Thus, an account's FICO score is a good proxy for its beta to systematic charge-off risk, as well as its expected default rate. Low FICO portfolios (600-650) have high net charge-off rates, between 8-10% per year, and are strongly exposed to fluctuations in aggregate charge-offs, with estimated betas between 1.3 and 1.6. In contrast, high FICO portfolios (800-850) have substantially lower net charge-off rates, between 1-3%, and much lower charge-off risk, with estimated betas between 0.2 and 0.6.

<a id='48bc3f44-52ce-4493-9713-da42421067b1'></a>

Second, we use the beta estimates to estimate the compensation for exposure to default risk, i.e., the default risk premium. To do so, we regress the ROA of FICO portfolio _i_ on its risk exposure, _β_i:

_ROA_i = _λ_ + _β_i_γ_ + _ν_i.
(2)

<a id='3016e40f-6712-4d83-8a56-9695ec9113ce'></a>

Thus, $\gamma$ is the compensation for exposure to systematic default risk, i.e., the default risk premium, and $\lambda$ is the average ROA on credit card account that has a zero beta to systematic default risk. $^{25}$

<a id='a28d16da-81b4-4037-9793-e0f120c7a4f2'></a>

Figure 12 and Table 4 present the ROAs, estimated risk premium β₁γ, and fitted ROA
(λ + βιγ) for each FICO portfolio based on equation (2). The results indicate that the
one-factor pricing model captures the ROA data very well, with the model's fitted ROAs

<a id='d57aabee-b81c-4784-84e8-c2fe0e478773'></a>

25We compute standard errors using the Newey-West correction with an optimal number of lags to account for potential autocorrelation and heteroskedasticity in the residuals. Our results are robust to clustering standard errors by time and origination FICO score bin in the pooled panel regression.

<a id='7102be07-90bf-403a-b003-c5c1eba7e8bc'></a>

35

<a id='c6108ad6-d008-4137-9b59-1c97ab55e1cb'></a>

aligning closely with actual ROAs across the entire range of FICO scores. Hence, exposure to aggregate default risk appears to fully explain the strong, increasing relation between FICO score and ROA.

<a id='4d49bbda-d243-445e-a42d-a206f25ad0a9'></a>

We find that the price of default risk, γ, is a highly significant 5.3% per year. Consequently, the estimated risk premium β_iγ ranges from 1.0-2.5% for the highest FICO portfolios (800-850) to 6.5-8.5% for the lowest FICO ones (600-680). Thus, the risk premium accounts for an increasing portion of the ROA as FICO score decreases.

<a id='f459dd8b-761f-40e6-8097-5dd13f6d0199'></a>

The intercept λ represents the regression's estimate of the ROA of a hypothetical zero-beta borrower, i.e, a borrower that has no exposure to systematic default risk. The estimate is 2.41%. Notably, this zero-beta rate estimate is close to the 2.57% ROA of the transactor portfolio, which carries no risk and thus has a zero beta, since it does not involve borrowing. Note that transactors were not included in the regression, and that they generate income through interchange and fees rather than interest charges. That their ROA aligns with the estimated zero-beta rate provides additional support for the view that the portion of ROAs in excess of this rate are compensation for risk.

<a id='40249883-2434-4d19-9eef-7c9ac67bf6b2'></a>

Next, we examine how our estimates of credit card default risk premiums compare to those observed in other markets. We focus on corporate bonds because the corporate bond market is very large and important, and because default rates on corporate bonds are highly sensitivity to the default cycle. Corporate bond credit spreads, defined as the difference between the yields on corporate debt and Treasury rates, have been found to be wider than is implied by expected default losses alone. This phenomenon, known as the credit spread puzzle, has been attributed to a credit risk premium that compensates investors for increased credit risk during economic downturns (e.g., Collin-Dufresn, Goldstein and Martin, 2001; Amato and Remolona, 2003).

<a id='c2f327ca-f7b0-4bce-9806-89c9efcfc096'></a>

To estimate the corporate bond credit risk premium, we use Mergent FISD historical
data on corporate bond issuance from 1990 to 2023. For each bond we track its history,
including its issuance details (date, amount and coupon), and whether and when the bond

<a id='cd2b1c55-1766-4e17-9509-0e3326f5776f'></a>

36

<a id='c123494d-b999-478b-b824-861cfa08192f'></a>

matured, defaulted or was called by the issuer. This allows us to construct the cash flows
paid to investors. In case of default, we assume a recovery rate of 40%, consistent with
Standard & Poor's (S&P) estimates.

<a id='4442f998-199f-496a-a108-6b584a98a907'></a>

Analogously with our approach for credit cards, we form monthly portfolios of bond investments based on their date of issuance and initial credit rating. We then compute the rating portfolios' buy-and-hold-to-maturity return. To adjust the returns for the risk-free return, we subtract from each bond's return the yield of a maturity-matched treasury as of the bond's issuance date. This gives us a monthly time series of default-adjusted credit spreads for each rating portfolio. The average of this time series is our estimate of the bond rating's default-adjusted credit spread. Our sample covers dollar-denominated corporate bonds that were issued and matured during 1990-2023.

<a id='02a48f01-3acb-45a7-9d44-15d5a8aad40d'></a>

To facilitate the comparison between bonds and credit cards, we map corporate bond ratings to FICO scores based on the 5-year expected default rates provided by S&P and our own calculations for credit cards. Figure 12 plots the credit card risk premia estimated from the one-factor model in Equation (2) (black line) and the default-adjusted credit spreads for the corporate bond portfolios (blue line). Remarkably, the corporate bonds' default-adjusted credit spread is very close to credit cards' risk premium across most of the ratings range.

<a id='a760c085-38fa-4a92-8a8f-d5d16acf0b9c'></a>

The exception are the lowest-rated bonds, those with a CCC/C rating. Their default frequency corresponds to a FICO score of around 620, at which point credit cards' risk premium exceeds the bonds' default-adjusted credit spread by a substantial 3%.

<a id='4a60ac4a-5b53-4453-90b7-91eb7a38918a'></a>

This gap opens up because there is a concave relationship between bonds' default frequency (which we map to a FICO score equivalent) and their estimated default-adjusted credit spreads. In contrast, the relationship between credit cards' FICO scores and their estimated risk premium is effectively linear (due to the near-linear relationship between FICO score and default beta). Thus, bond credit spreads are a bit higher than credit cards' risk premium for the highest rating (BBB), are the same at intermediate ratings (BB), and are lower at the lowest rating (CCC/C).

<a id='863860eb-5e89-45a6-b5d0-0f88bcb895e8'></a>

37

<a id='a8f66a9b-567e-473f-b238-f349e25b9398'></a>

One caveat is that the credit card risk premia are likely estimated much more precisely than the default-adjusted bond spreads. There are two reasons for this. First, we have a far finer gradient of FICO scores than bond ratings; there are 50 FICO bin portfolios, one for every 5 FICO point increment between 600 and 850, compared to only 4 ratings portfolios. Second, there are many more credit card accounts than bond issuers. Our sample contains hundreds of millions of unique credit card borrowers, versus 10,025 unique bond issuers, of which only 540 were issuers of CCC/C-rated bonds. Thus, there is a lot more idiosyncratic noise in the bond portfolio returns, especially the lowest-rated ones where large individual defaults can affect the average, than in the credit card portfolios, which are composed of millions of small accounts.

<a id='57014232-fe5c-47ba-9ad5-1b9095501012'></a>

Nevertheless, it is unlikely that noise accounts for most of the roughly 3% gap between the default-adjusted spread of CCC/C-rated bonds and the corresponding credit card risk premium, as we are not aware of any estimate of the CCC/C default-adjusted spread that places it close to the estimated 8% risk premium on the corresponding credit cards. Thus, our results suggest that, compared to the corporate bond market, credit card banks likely earn an excess risk premium on the low FICO-score accounts.

<a id='50bad661-b6ee-4887-93a1-bfa47280dd2a'></a>

Finally, we compare the zero-beta rate of credit cards, which represents their return ad-justed for default risk to the ROA of the entire U.S. banking sector. Using Call Report data over our sample period, we estimate the banking sector's pre-tax ROA to be approximately 1.5%. Comparing this to the 2.41% zero-beta rate implies that credit cards yield a 0.9% higher default-risk-adjusted ROA than the overall banking sector. This estimate represents a lower bound on the difference because the banking sector has a small default risk. Across commercial banks, average charge-offs amount to about 0.25% of total assets, or 0.5% of loans and leases. Based on the relationship between average charge-offs and default-risk betas estimated from the FICO portfolios in Figure 11, we estimate that bank assets have a beta in the range of 0.05 to 0.1, translating to a default-risk premium of approximately 0.26% to 0.53%. Using this estimate implies that credit cards' zero-beta rate is 1.17% to

<a id='382421ba-b123-4926-9658-7000fa26c6be'></a>

38

<a id='d5bf5a70-9df9-46dc-99bc-2b60f977388b'></a>

1.44% higher than the default-risk-adjusted ROA of the overall banking sector.

<a id='530dbddd-2e93-4ea9-9f5b-9fa06c58b6cb'></a>

## 5.1 Can Capital Requirements Explain the High ROAs?

In this section, we examine whether bank capital regulation can explain the high ROA of the credit card portfolios. Basel III, the main bank capital regulation, mandates that banks maintain minimum equity capital equal to a given percentage of risk-weighted assets (RWA), in order to absorb potential losses. The regulation assigns risk-weights based on an asset's risk, so that banks must maintain more capital for riskier exposures. For instance, cash and government bonds are very safe, so they carry a 0% risk weight. In contrast, corporate loans and credit card debt are risky and hence have much higher risk weights.

<a id='2e5a8ef6-f199-4c42-9783-ca195ee4fae2'></a>

Hence, if credit card loans have a higher risk weight than the average asset, banks' cost of regulatory capital will be higher for these risky assets and they will need to earn a higher ROA on them to cover this cost of regulatory capital. This regulatory hurdle rate is higher for low-FICO credit card lending because it is the riskiest type of credit card lending and hence has the highest risk weight. Thus, the combination of regulatory risk weights and the cost of regulatory capital could in principle explain the ROA of credit card lending and why it declines in FICO score.

<a id='b6f432c1-421c-4255-943e-aca0e022fa86'></a>

To test this hypothesis, we calculate the regulatory risk weights for credit card loans and their implied cost of regulatory capital across the range of FICO scores. Credit card exposures fall under retail credit risk, and are assigned different risk weights depending on whether an account is classified as a transactor or a borrower, with borrowers having higher risk weights. 26 The risk weights also depend on whether a bank is using the so called "standardized approach", defined by the Basel Committee, or the "advanced approach", which relies on internal risk models. The advanced approach is used by large banks with total consolidated assets of $250 billion or more, while the standardized approach is used

<a id='b7c3a4f0-e10b-40b7-936a-542900d6b3c9'></a>

26 Similar to our definition, regulators classify accounts that repay their balance in full each month as transactors, and define borrowers as accounts who carry revolving balances.

<a id='44874974-8397-445e-a724-730918f7a12b'></a>

39

<a id='cc190444-854c-48b4-8179-3e6cba548996'></a>

by the smaller banks.27
Under the standardized approach, risk weights are fixed at 45% for transactors and 75% for borrowers. In contrast, under the advanced approach, risk weights are determined based on banks' internal assessments of an account's probability of default (PD) and loss given default (LGD), following Basel III formulas. However, they are subject to lower bounds of 45% for transactors and 75% for borrowers, as in the standardized approach. 28 The risk weight for borrowers under the advanced approach in Basel III regulation is given by:

<a id='d9c4bfb0-035a-46ee-a330-19927e9a4fc9'></a>

$\max \left\{ 0.75, 12.5 \cdot \left[ LGD \cdot N \left( \frac{G(PD)}{\sqrt{1 - 0.04}} + \sqrt{\frac{0.04}{1 - 0.04}} \cdot G(0.999) \right) - PD \cdot LGD \right] \right\}$

<a id='c6a9dec3-0795-4d45-b4d3-4859ab03a700'></a>

For transactors, it is defined as:

$\max \left\{ 0.45, 12.5 \cdot \left[ LGD \cdot N \left( \frac{G(PD)}{\sqrt{1 - 0.04}} \right) + \sqrt{\frac{0.04}{1 - 0.04}} \cdot G(0.999) - PD \cdot LGD \right] \right\}$

<a id='492b014f-264b-4554-8fdf-523532aa83cb'></a>

where $N(x)$ is the cumulative distribution function of a standard normal variable and $G(z)$ is its inverse.

<a id='3622cdda-585b-4b52-b672-e6b5655646ad'></a>

Using account-level data on PD and LGD from the Y-14M data, we calculate the risk weights for each origination FICO bin, separately for transactors, borrowers, and all users. Figure 13a illustrates these risk weights, showing that they are clearly decreasing in FICO score. Notably, borrowers' risk weights are more than twice as high as those of transactors, ranging from around 75% for the highest FICO accounts to 140% for the riskiest borrowers.

<a id='f8a64909-662e-4999-8be2-34686bdd5b0a'></a>

Next, we compare the ROA of credit card lending for each FICO score to its cost of regulatory capital. We estimate this cost by multiplying the risk weight for credit card loans at the FICO score by banks' cost of regulator capital. We estimate banks' cost of

<a id='c842bf1b-29db-4acd-b59b-ae398d0f6c63'></a>

27 We classify banks in the Y-14M sample based on their approach to the risk-weight calculation. We classify banks that do not report internally estimated variables, such as probability of default (PD), as standardized approach banks, and those that do report these variables as advanced approach banks.
28 Under the advanced approach, risk weights for borrowers tend to be higher than under the standard-

<a id='50be44f6-30c3-4d6d-b538-3593c65c4438'></a>

ized approach. For transactors, however, the standardized approach's 45% risk weight usually binds due
transactors' low PDs.

<a id='d9669302-79ec-4668-8346-75d178fee4ac'></a>

40

<a id='dd3ba052-563a-4ce6-9cc6-9be92cae3c2a'></a>

regulatory capital as the banking sector's ROA per risk-weighted asset. This value gives banks' cost of regulatory capital assuming that banks' ROA is the minimum return that covers their cost of regulatory capital. Otherwise, banks' ROA is higher than needed to cover the cost of their regulatory capital and our measure is an upper bound on the cost of regulatory capital.

<a id='39df92ed-722e-4251-b556-d531d832f8ad'></a>

From the Call Reports, we compute the average risk weight of banks by dividing the banking sector's total Risk-Weighted Assets (RWA) by total assets. We find that the average risk weight is 70%. This is higher than the risk weight for transactors and substantially lower than the risk weights for borrowers with low FICO scores.

<a id='2a00fa86-d637-428d-a54c-783f5c62a415'></a>

From the Call Reports we also estimate banks' pre-tax ROA to be 1.5%. Dividing this
value by the 70% average risk weight gives an average pre-tax ROA per risk weight of 2.14%.
Multiplying this value by credit cards' risk weight gives their cost of regulatory capital at
each FICO score.

<a id='2674ffb0-0ef8-475e-b15b-abd7d78c2f75'></a>

These values are plotted in Figure 13b, together with the ROAs on borrowers. The figure makes clear that credit cards' ROAs are much higher than their cost of regulatory capital. Therefore, the cost of regulatory capital does not explain the ROAs on credit card lending. This result is not surprising once we see that credit cards' risk weights are 'only' 75% to 140%, or one to two times the risk weight of the average bank asset, since credit card ROAs are 3-5 times bank's aggregate ROA. Thus, credit card ROAs are much higher than is required to meet their regulatory capital requirements.

<a id='366f68ad-d84a-455d-8473-92f96b48d722'></a>

## 6 Conclusion

Credit card interest rates are significantly higher than those on other forms of lending, with an average APR of 23% in 2023-an 18% spread over the Fed funds rate. In this paper, we investigate why these rates are so high and, more broadly, how credit card banking operates. This question is particularly important given that credit cards are the primary

<a id='1435002f-d9c2-429c-8b92-9adce147d9c6'></a>

41

<a id='15844e44-a94c-431d-a21c-d019d2d84795'></a>

method of unsecured borrowing for consumers, with 60% of accounts carrying a balance.
With more than $1.1 trillion outstanding balances and generating 16.6% of banks' interest
income despite comprising only 4.5% of bank assets, understanding the factors driving credit
card pricing has broad implications for financial markets.

<a id='90487f0e-e61b-4a0f-b3f8-8f712a944f46'></a>

To answer this research question, we use the most comprehensive and granular dataset, covering 330 million credit card accounts from the 20 largest banks in the US, representing over 90% of total credit card lending. We examine four potential explanations for high credit card rates: compensation for default losses, the cost of rewards programs, a large default risk premium, and market power. Our findings show that while charge-offs are substantial, they do not fully explain the high APR spreads; banks maintain an average default-adjusted spread of 10% after accounting for the defaults. Non-interest expenses, such as rewards, are substantial but offset by corresponding non-interest income, such as interchange. Instead, market power plays a significant role, with banks incurring large operating expenses especially in marketing to acquire and retain customers. In addition, undiversifiable default risk is a major driver of pricing, as credit card charge-offs are highly cyclical and correlated with broader economic downturns. We estimate the risk premium component of credit card return using the cross-section of accounts by default likelihood. We find that risk premium can explain the large cross-sectional differences in net lending margins, with the average borrower commanding a 5.3% risk premium, similar to that in high-yield bonds. After adjusting for risk premium, we find that credit card lending still generates "alpha" of approximately 1.17% to 1.44% compared to the overall banking sector.

<a id='1253a442-644b-4368-96ad-4540a4a0edb9'></a>

Our findings highlight the distinct economics of credit card lending, where high interest rates reflect more than just default losses—risk premium and market power play a central role. Looking beyond this paper, several promising directions for future research remain. For instance, it would be fruitful to explore how competition and regulation influence credit card banking and how it interacts with emerging forms of consumer credit.

<a id='d921156f-e6de-4de1-a072-de564104cd4d'></a>

42

<a id='1eb2184e-801e-46b1-ac1e-b5d40a8b3ffc'></a>

References

**Agarwal, Sumit, Andrea Presbitero, André Silva, and Calo Wix.** 2022. “Who Pays For Your Rewards? Cross-Subsidization in the Credit Card Market.” *Working Paper.*
**Agarwal, Sumit, Souphala Chomsisengphet, Neale Mahoney, and Johannes Stroebel.** 2015. “Regulating Consumer Financial Products: Evidence from Credit Cards.” *The Quarterly Journal of Economics*, 130(1): 111–164.
**Amato, Jeffery D, and Eli M Remolona.** 2003. “The credit spread puzzle.” *BIS Quarterly Review, December.*
**Ausubel, Lawrence.** 1991. “The Failure of Competition in the Credit Card Market.” *The American Economic Review*, 81(1): 50–81.
**Berlin, Mitchell, and Loretta J Mester.** 2004. “Credit card rates and consumer search.” *Review of Financial Economics*, 13(1-2): 179–198.
**Calem, Paul, and Loretta Mester.** 1995. “Consumer Behavior and the Stickiness of Credit-Card Interest Rates.” *The American Economic Review*, 85(5): 1327–1336.
**CMSPI.** 2024. “State of the Industry Report.” *White Paper.*
**Collin-Dufresn, Pierre, Robert S Goldstein, and J Spencer Martin.** 2001. “The determinants of credit spread changes.” *The Journal of Finance*, 56(6): 2177–2207.
**Consumer Financial Protection Bureau.** 2023. “The Consumer Credit Card Market.” *Report.*
**Cordell, Larry, Michael R Roberts, and Michael Schwert.** 2023. “CLO performance.” *The Journal of Finance*, 78(3): 1235–1278.
**Drechsler, Itamar, Alexi Savov, and Philipp Schnabl.** 2017. “The Deposits Channel of Monetary Policy.” *The Quarterly Journal of Economics*, 132(4): 1819–1876.
**Drechsler, Itamar, Alexi Savov, and Philipp Schnabl.** 2021a. “Banking on Deposits: Maturity Transformation without Interest Rate Risk.” *The Journal of Finance*, 76(3): 1091–1143.

<a id='1deb8cc3-88a2-4eb8-ad67-b60379fa7b71'></a>

43

<a id='428ea245-30e1-4498-8690-f0bf89871357'></a>

Drechsler, Itamar, Alexi Savov, and Philipp Schnabl. 2021b. "Banking on De-posits: Maturity Transformation without Interest Rate Risk." The Journal of Finance, 76(3): 1091-1143.

Drozd, Lukasz, and Jaromir Nosal. 2008. "Competing for Customers: A Search Model of the Market for Unsecured Credit." Working Paper.

Erel, Isil, Thomas Flanagan, and Michael S Weisbach. 2024. "Risk-Adjusting the Returns to Private Debt Funds." National Bureau of Economic Research.

Fama, Eugene F, and James D MacBeth. 1973. "Risk, return, and equilibrium: Em-pirical tests." Journal of political economy, 81(3): 607-636.

Flanagan, Thomas. forthcoming. "The value of bank lending." Journal of Finance.

Fleckenstein, Matthias, and Francis A. Longstaff. 2022. "The Market Risk Premium for Unsecured Consumer Credit Risk." The Review of Financial Studies, 35(10): 4756-4801.

Galenianos, Manolis, and Alessandro Gavazza. 2018. "Regulatory intervention in consumer search markets: The case of credit cards." Working paper.

Gupta, Arpit, and Stijn Van Nieuwerburgh. 2021. "Valuing private equity investments strip by strip." The Journal of Finance, 76(6): 3255-3307.

Han, Song, Ben Keys, and Geng Li. 2018. "Unsecured Credit Supply, Credit Cycles, and Regulation." The Review of Financial Studies, 31(3): 1184-1217.

Herkenhoff, Kyle, and Gajendran Raveendranathan. 2021. "Who Bears the Welfare Costs of Monopoly? The Case of the Credit Card Industry." NBER Working Paper, http://www.nber.org/papers/w26604.

Kaplan, Steven N, and Antoinette Schoar. 2005. "Private equity performance: Re-turns, persistence, and capital flows." The journal of finance, 60(4): 1791-1823.

Korteweg, Arthur, and Stefan Nagel. 2016. "Risk-adjusting the returns to venture capital." The Journal of Finance, 71(3): 1437-1470.

Nelson, Scott. 2024. "Private information and price regulation in the us credit card mar-

<a id='0955d321-fb1d-492e-beda-7c620a20b56b'></a>

44

<a id='7b7dd3a4-7b79-48ab-a84d-caafb96da327'></a>

ket.” Econometrica.

<a id='62374e14-373e-445a-97ce-83e894943bb3'></a>

**Neumark, David, and Steven A Sharpe.** 1992. "Market structure and the nature of price rigidity: evidence from the market for consumer deposits." *The Quarterly Journal of Economics*, 107(2): 657–680.

**Stango, Victor, and Jonathan Zinman.** 2016. "Borrowing High versus Borrowing Higher: Price Disperson and Shopping Behavior in the U.S. Credit Card Market." *The Review of Financial Studies*, 29(4): 979–1006.

<a id='5edb5e45-4205-41ee-86f1-b7d88d8dd145'></a>

**Zhou, Guanyu**. 2025. "How Much Did Credit Card Banks Benefit from the Covid Checks?"
*Working Paper*.

<a id='ad568e8a-7fbc-4fc9-b6b7-247c5cd2eb13'></a>

45

<a id='6e697f87-031d-43d9-b7d6-024af3411cb5'></a>

Figures

<a id='b8119a66-06be-4220-9a53-37238caa04c5'></a>

Figure 1: Distribution of accounts by origination FICO score

<a id='5a4d9aee-4207-4495-b0e6-3809df853836'></a>

This figure presents the distribution of observations in our sample based on FICO scores at account origination, with accounts grouped into 5-point FICO bins. The sample consists of accounts originated between January 2015 and December 2018, which we track from origination through December 2023. The new account share (blue line) represents the proportion of accounts within each FICO bin at the time of origination, relative to the total number of originated accounts in the sample. The account share (red line) reflects the proportion of account-month observations associated with each FICO bin, relative to the total number of observations over the sample period. The balance-weighted account share (green line) captures the proportion of lifecycle balances (average daily balances) held by accounts in each FICO bin, relative to the total balance, defined as the sum of all balances across all accounts over their lifetime. Further details on sample construction are provided in Section 2.1.

<a id='ca22492c-7d30-4bf8-baa6-2d9b917fdbee'></a>

<::Line chart showing 'share' on the y-axis and 'FICO at Account Origination' on the x-axis. The y-axis ranges from 0 to .035, with major ticks at 0, .005, .01, .015, .02, .025, .03, and .035. The x-axis ranges from 600 to 850, with major ticks at 600, 650, 700, 750, 800, and 850. Three lines are plotted:
- A blue line representing 'new account share'.
- A red/purple line representing 'account share'.
- A green line representing 'balance weighted account share'.

All three lines generally increase from FICO 600 to around 675-700, then decrease towards FICO 850. The 'balance weighted account share' (green line) is notably higher than the other two lines between FICO 675 and 750, peaking around .034, while the 'new account share' and 'account share' lines peak around .026 in the same range. The 'new account share' and 'account share' lines track very closely together throughout the chart.::>

<a id='242e2152-0da6-464b-bb90-b50ad8aa3a8e'></a>

46

<a id='b1be4574-d694-481d-aa3c-ebca24e47aeb'></a>

Figure 2: Distribution of borrowers and balances by FICO score at origination
Panel (a) shows the distribution of observations and total balances attributed to borrowers in our sample, grouped by FICO scores at account origination in 5-point bins. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. The equal-weighted borrower share (blue line) represents the proportion of monthly active account-level observations classified as borrowers. The balance-weighted borrower share (red line) represents the share of the bank's total credit card balance held by borrower accounts. Panel (b) displays the Average Daily Balance (ADB, in dollars) for borrowers (blue line) and active transactors (red line), grouped by FICO scores at account origination in 5-point bins. Active transactors are accounts that do not revolve a balance (i.e., are not borrowers) but remain active, meaning they exhibit a positive cycle-ending balance, purchase volume, or payment activity in a given month.

<a id='d34f55cf-c97e-44b8-bdfd-3ace123c0607'></a>

<::Two line charts are presented. The top chart, labeled "(a) Borrower Share," displays "Share (among active accounts)" on the y-axis, ranging from 0.2 to 1.0, and "FICO at Origination" on the x-axis, ranging from 600 to 850. It shows two lines: a blue line representing "Borrower share (equal weighted)" which starts around 0.8 and gradually decreases to below 0.3, and a red line representing "Borrower share (balance weighted)" which starts near 0.95 and decreases to around 0.45. The bottom chart, labeled "(b) Borrower vs. Transactor ADB," displays "Average Daily Balance" on the y-axis, ranging from 0 to 4500, and "FICO at Origination" on the x-axis, ranging from 600 to 850. It also shows two lines: a blue line representing "Borrower" which starts around 1800, increases to over 4000, and then slightly decreases, and a red line representing "Active Transactor" which starts near 200 and gradually increases to over 1000.
: chart::>

<a id='ab1fd3f0-47bc-46c8-86a8-f64937c42c3f'></a>

47

<a id='2eddd126-ac6e-4742-a85f-f937c761e80b'></a>

Figure 3: Distribution of effective interest rates paid by borrowers
This figure shows the 25th percentile (dashed red line), average (solid blue line), and 75th percentile (dashed green line) of the effective interest rates paid by borrowing accounts within each FICO score bin at origination. The sample is restricted to observations where the account is classified as a borrower, which is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. The effective interest rate is calculated as the reported finance charge divided by the borrower's Average Daily Balance (ADB), with all rates annualized. The average interest rate is weighted by the ADB of borrowers within each FICO bin.

<a id='0c00fa03-c353-44b1-9d22-e572fb48d846'></a>

<::Line chart showing Interest Income Rate versus FICO at Origination. The Y-axis, labeled "Interest Income Rate", ranges from 0 to 0.25. The X-axis, labeled "FICO at Origination", ranges from 600 to 850. There are three lines representing different borrower percentiles:
- A solid blue line represents "Borrower: avg".
- A dashed red line represents "Borrower: p25".
- A dashed green line represents "Borrower: p75".

The "Borrower: avg" line starts around 0.22 at FICO 600 and gradually decreases to around 0.09 at FICO 850.
The "Borrower: p25" line starts around 0.21 at FICO 600, decreases sharply from FICO 650 to 750, and then remains near 0 from FICO 750 to 850.
The "Borrower: p75" line starts around 0.25 at FICO 600 and gradually decreases to around 0.15 at FICO 850.
: chart::>

<a id='8efd860b-3ceb-446d-bb15-acd0222338fb'></a>

48

<a id='90b89ce3-d10e-41f3-882d-f539c6f01037'></a>

Figure 4: Net interest income, charge-offs and default-adjusted credit spread for borrowing accounts

This figure plots interest income (blue area), interest expense (red area), and credit losses (green area), all on the left y-axis, alongside the default-adjusted credit spread (black line on the right y-axis) for borrowers, grouped by FICO scores at account origination in 5-point bins. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. For each FICO bin, we calculate lifetime Average Daily Balance (ADB), interest income, interest expense, and net credit losses by aggregating these variables across all borrowing accounts in the bin over the entire sample period. Interest income represents the account's finance charge. Interest expense is computed by multiplying the account's ADB by the federal funds rate for the corresponding month. Net credit loss is calculated as charge-offs minus recoveries, where charge-offs are attributed to default or bankruptcy. We derive the respective rates by dividing lifetime interest income, interest expense, and net credit loss by lifetime ADB. The default-adjusted credit spread is then defined as the interest income rate minus the interest expense rate and net credit loss rate. All rates are annualized.

<a id='65713725-fbee-4eb6-864f-0225d181a739'></a>

<::chart: The chart displays several financial metrics against "FICO at Account Origination" on the x-axis, ranging from 600 to 850. The left y-axis represents "Share of Lifetime ADB" from -0.15 to 0.25. The right y-axis represents "Default Adjusted Credit Spread" from 0.06 to 0.13. The chart includes four data series:
- **Interest Income**: Represented by a blue shaded area, showing positive values that generally decrease as FICO increases.
- **Interest Expense**: Represented by a red shaded area, showing a relatively constant value near zero.
- **Net Credit Loss**: Represented by a green shaded area, showing negative values that become less negative (increase) as FICO increases.
- **Default Adjusted Credit Spread**: Represented by a black line, plotted against the right y-axis, showing a decreasing trend as FICO increases.

Legend:
- Blue box: Interest Income
- Red box: Interest Expense
- Green box: Net Credit Loss
- Black line: Default Adjusted Credit Spread (right axis)::>

<a id='20c8bc0b-53b6-430f-ba0a-c5b061f669f7'></a>

49

<a id='7b720785-7c84-4e1c-a8df-e72402a6f3a4'></a>

Figure 5: Purchase volumes by borrowers and transactors This figure plots the average monthly purchase volume (in US dollars) for borrowers and active transactors, grouped by FICO scores at account origination in 5-point bins. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Active transactors are accounts that do not revolve a balance (i.e., are not borrowers) but remain active, meaning they exhibit a positive cycle-ending balance, purchase volume, or payment activity in a given month. <::chart: Line chart showing Purchase Volume (in US dollars) on the Y-axis, ranging from 200 to 1800, and FICO at Origination on the X-axis, ranging from 600 to 850. There are two lines plotted: a blue line labeled "Borrower" and a red line labeled "Active Transactor". The "Borrower" line starts around 220 at FICO 600 and steadily increases to approximately 1280 at FICO 850. The "Active Transactor" line starts around 650 at FICO 600 and generally increases, with some fluctuations, to approximately 1600 at FICO 850. The "Active Transactor" line is consistently above the "Borrower" line across the entire FICO range.::>

<a id='7a2f52b5-169c-4f14-8b66-2fe9eb7260ba'></a>

50

<a id='8f2d3101-edae-48a0-8253-01f804758b3c'></a>

Figure 6: Interchange and rewards for borrowers and transactors

This figure plots interchange income (yellow area), rewards expenses (purple area), both on the left y-axis, and net interchange income, defined as interchange – rewards (black line, on the right y-axis). All variables are computed as a share of Average Daily Balance (ADB) and grouped by FICO scores at account origination in 5-point bins. To compute these variables, we proceed in four steps. First, we use Y-14's account-level data to calculate bank-level purchase volume by aggregating the purchase volume of the individual accounts during the month. Second, we use bank-level information on total interchange income, reward expenses from the Y-14's portfolio-level data as well as the purchase volumes from the first step to compute the interchange and reward rates by dividing the dollar value of interchange/rewards for the bank by the bank's purchase volume. Third, we compute interchange income and rewards expense at the origination FICO score bin level by multiplying the interchange and rewards rates, derived from portfolio-level data in the second step, by the cumulative lifetime purchase volume of all accounts within the FICO score bin over the entire sample. Fourth, we compute the interchange income and reward expense as a share of Average Daily Balance (ADB) by dividing the cumulative monthly dollar amount of interchange and rewards in a given FICO bin by their cumulative ADB. All values are annualized. We do it separately for transactors, depicted in panel (a), and borrowers, shown in panel (b). A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Transactors are accounts that do not revolve a balance (i.e., are not borrowers). Appendix A.1 provides a detailed description of how we compute both rates.

<a id='aa1a5791-93d8-4182-8078-e19d71c77e03'></a>

<::(a) Transactors: A combined area and line chart showing Share of Lifetime ADB on the left y-axis and an unlabeled axis (implied to be Net Interchange) on the right y-axis, against FICO at Account Origination on the x-axis. The x-axis ranges from 600 to 850. The left y-axis ranges from -0.4 to 0.6, with tick marks at -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6. The right y-axis ranges from 0 to 0.14, with tick marks at 0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14. The chart displays three data series: Interchange Income (yellow shaded area, positive values), Rewards Expense (purple shaded area, negative values), and Net Interchange (green line, plotted against the right axis). The yellow area for Interchange Income starts around 0.55 at FICO 600 and gradually decreases to about 0.3 at FICO 850. The purple area for Rewards Expense starts around -0.4 at FICO 600 and gradually increases to about -0.3 at FICO 850. The green line for Net Interchange starts around 0.13 at FICO 600, fluctuates, stays mostly between 0.06 and 0.08 until around FICO 800, then drops sharply to below 0 at FICO 850.: chart::>

<a id='80f80191-98ed-4253-bf18-cebf22969d21'></a>

<::(b) Borrowers: A line and area chart showing Share of Lifetime ADB and Net Interchange against FICO at Account Origination. The x-axis, 'FICO at Account Origination', ranges from 600 to 850. The left y-axis, 'Share of Lifetime ADB', ranges from -0.08 to 0.08. The right y-axis, 'Net Interchange (right axis)', ranges from -0.001 to 0.008. The chart displays three components: Interchange Income (yellow area), Rewards Expense (purple area), and Net Interchange (green line). Interchange Income starts around 0.03 at FICO 600 and increases to approximately 0.075 at FICO 850. Rewards Expense starts around -0.02 at FICO 600 and decreases to approximately -0.07 at FICO 850. Net Interchange starts around 0.008 at FICO 600, decreases sharply to around 0.002 by FICO 650, fluctuates between 0.002 and 0.005 until FICO 800, then drops sharply to below -0.001 at FICO 850.: chart::>

<a id='f0d5d441-3a95-4af3-aae1-72ec6e553adc'></a>

Figure 7: Bank operating expenses and their relationship with borrower interest spreads and gross margins

<a id='a2c712f2-43f4-4994-9d59-7d0b170cd93b'></a>

Panel (a) presents a scatter plot of borrowers' interest spreads against bank-level operating expense rates, with separate data points for portfolios originating at FICO scores of 650 (blue), 700 (red), and 750 (green). Borrower interest spread is calculated as total finance charges minus interest expenses across all borrower observations within a bank-origination FICO bin, divided by the total borrower Average Daily Balance (ADB) in that bin. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Operating expense rate is the total operating expense divided by the total cycle-ending balance, measured at the bank-month level and averaged over the sample period from January 2015 to December 2023. The size of each bubble represents the relative total borrower ADB within its origination FICO bin. The yellow line represents the fitted regression line from regressing the borrower's interest spread rate on the operating expense rate, controlling for origination FICO fixed effects. The regression is weighted by borrower ADB. Panel (b) follows the same structure as Panel (a) but replaces the y-axis variable with gross margin for all accounts within a bank-origination FICO bin. Gross margin is defined as the net interest spread plus net interchange and fee income, minus net charge-offs and other non-operating expenses (e.g., fraud). All rates are annualized.

<a id='75a260f1-be82-4c24-abe3-3ed282ac1baf'></a>

(a) Interest Spread
<::chart: A scatter plot titled "(a) Interest Spread" shows "Borrower Interest Spread" on the y-axis and "Operating Expenses" on the x-axis. The plot contains data points represented by circles of varying sizes, colored blue, red, and green. A legend indicates that blue points correspond to "650", red points to "700", and green points to "750". A black line labeled "Fitted Borrower Interest Spread" is also present, showing a positive linear trend. The y-axis ranges from .08 to .22, and the x-axis ranges from 0 to .1.::>
(b) Gross Margin

<a id='50e4d37f-6da4-4a89-908f-40eb2226f595'></a>

<::(b) Gross Margin: A scatter plot titled "(b) Gross Margin" shows Gross Margin on the y-axis, ranging from 0.06 to 0.22, and Operating Expenses on the x-axis, ranging from 0 to 0.1. The plot displays data points as circles of varying sizes and colors. A legend indicates that blue circles correspond to a value of 650, red circles to 700, and green circles to 750. A black line, labeled "Fitted Gross Margin," represents a linear fit through the data points.: chart::>

<a id='dbd51f1b-c82f-4b60-911c-5b870b650fd5'></a>

Figure 8: Return on Assets: Borrowers

This figure presents all income and expense components (all on the left y-axis) along with return on assets (ROA) (black line on the right y-axis) for borrowers, grouped by FICO scores at account origination in 5-point bins. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Income components are plotted as positive values, while losses and expenses appear as negative values. Interest income, interest expense and credit loss are computed as in Figure 4. Non-interest income includes interchange income as computed in Figure 6b plus fee income. Non-interest expense includes rewards income in Figure 6b plus operating expenses, interchange expenses and fraud. All lifetime average rate variables are constructed following the methodology in Section 4: for each origination FICO bin, we compute the cumulative lifetime dollar amount of each component across all accounts in the bin over the entire sample period, then divide it by their cumulative Average Daily Balance (ADB). ROA (net margin) is defined as interest spread minus net charge-offs, plus net interchange income (interchange minus rewards), plus the fee income rate, minus the operating expense rate and other non-operating expenses. All rates are annualized.

<a id='76349a17-16dd-4257-bc01-a9176d585859'></a>

<::This is a stacked area chart with an overlaid line graph. The x-axis is labeled "FICO at Account Origination" and ranges from 600 to 850. There are two y-axes. The left y-axis is labeled "Share of Lifetime ADB" and ranges from -0.2 to 0.3. The right y-axis is labeled "ROA" and ranges from 0.05 to 0.11. The stacked areas represent different components of the "Share of Lifetime ADB": Interest Income (blue), Non-Interest Income (yellow), Interest Expense (red), Credit Loss (green), Non-Interest Expense (purple), and Operating Expense (dark blue/grey). The black line graph represents "ROA (right axis)", which generally decreases as FICO at Account Origination increases, with a sharp drop around FICO 675.::>

<a id='8d1ba929-7a02-479f-b5b1-50c527c5302e'></a>

53

<a id='0f4463de-83ea-4301-abb6-bd142c2fdf62'></a>

Figure 9: Default rates across various types of loans and corporate bonds
This figure presents the time series of charge-off rates for various types of loans and corporate bonds. Panel
(a) displays the net charge-off rates for credit cards, other consumer loans, commercial and industrial (C&I)
loans, single-family residential mortgages, and commercial real estate loans, sourced from FRED. The U.S.
corporate bond default rate is obtained from Standard & Poor's (S&P), which reports the number of issuers
that defaulted in a given period divided by the total number of issuers at the beginning of that period.
Panel (b) shows the comparison between the U.S. speculative-grade corporate bond default rate from S&P
and the credit card charge-off rate.

<a id='221100c7-f576-42aa-80f7-caaa04c516c1'></a>

<::(a) Bank loans: line chart::>  <::The chart displays the Charge-off Rate on the y-axis, ranging from 0 to 10, against years on the x-axis, from 1985 to 2025.::>  <::Legend: Credit Card Loans (black line), Residential Mortgages (green line), Other Consumer Loans (blue line), Commercial Mortgages (orange line), C&I Loans (purple line), US Corporate Bonds (red line).::>

<a id='c08025cf-106c-43f6-b377-7869280466fb'></a>

(b) Credit cards and corporate bonds<::Line chart showing Default Rate (%) on the y-axis and time (from 1985q1 to 2025q1) on the x-axis.Two lines are plotted:1. Red line: Charge-Off Rate on Credit Card Loans2. Blue line: US Speculative Grade Corporate Default RateThe y-axis ranges from 2 to 12.Both rates show fluctuations over time, with notable peaks around 1991, 2001-2002, 2008-2010, and 2020-2021. The US Speculative Grade Corporate Default Rate (blue line) generally shows higher peaks than the Charge-Off Rate on Credit Card Loans (red line).: chart::>

<a id='44cb0740-4eba-4517-8579-9a4d2da7681d'></a>

54

<a id='5d6b44ba-aa7d-4808-b4e7-ed126248becc'></a>

Figure 10: Credit card charge-off dynamics: account life cycle and time series trends

<a id='00f8f157-13f9-404f-a4f3-75df3ec7bc68'></a>

This figure plots the charge-off rates for selected groups of borrower accounts with different origination FICO scores, analyzed by account age (months since origination) and over time. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Panel (a) shows the charge-off rate by account age for accounts originated in 2016 across five different FICO scores at origination (600 in blue, 660 in red, 700 in green, 760 in yellow, 800 in purple). At each account age, the charge-off rate is calculated as the total borrower charge-offs at that age divided by the total borrower Average Daily Balance (ADB) at the same age. Panel (b) presents the time series of charge-offs across five different origination FICO scores. At each point in time, the charge-off rate is computed by taking the total borrower charge-offs and dividing it by the total borrower ADB within the specific origination FICO bin and month. All rates are annualized.

<a id='9ac013b8-2c30-4189-bfd8-865cc9b8857f'></a>

<::chart: (a) Life cycle. This line chart shows Charge-off (due to default) as Share of ADB on the y-axis, ranging from 0 to 0.25. The x-axis represents Months since Origination (2016 cohort), ranging from 0 to 100. There are five lines, each representing a different value: 600 (blue), 660 (red), 700 (green), 760 (yellow), and 800 (purple). The lines generally show an initial increase in charge-off, followed by a decrease, and then a slight increase towards the end of the period.::> <::chart: (b) Time series. This line chart shows Charge-off (due to default) as Share of ADB on the y-axis, ranging from 0 to 0.16. The x-axis represents time from 2015m1 to 2023m1. There are five lines, each representing a different value: 600 (blue), 650 (red), 700 (green), 750 (yellow), and 800 (purple). The lines show fluctuations over time, with a general downward trend from late 2019 to early 2022, followed by an upward trend.::>

<a id='9a30bb9e-b1de-4c02-b81d-616ceaaff1b5'></a>

55

<a id='798cb7ab-3e42-465d-a1e3-6781175be08d'></a>

Figure 11: Risk exposure by origination FICO score
This figure plots the estimates of the risk exposure, beta, for each origination FICO bin (black line, right y-axis) and their actual charge-off rate (blue line, left y-axis). For each FICO bin, we estimate its beta to systematic default risk by regressing the change in its monthly charge-off rate on the change in the charge-off rate of the aggregate credit card portfolio by following specification 1. Charge-off rate is defined the same as in Figure 4.
<::chart: A line chart titled "Risk exposure by origination FICO score" displays two lines against an x-axis labeled "Origination FICO" ranging from 600 to 850.
The left y-axis is labeled "charge-off rate" and ranges from .01 to .1.
The right y-axis is labeled "beta" and ranges from .2 to 1.8.

- The blue line represents the "charge-off rate (left)", starting around .1 at FICO 600 and generally decreasing to approximately .02 at FICO 850.
- The black line represents "beta (right)", starting around .9 at FICO 600, fluctuating, and generally decreasing to approximately .3 at FICO 850.::>

<a id='b9a6e7b6-842f-42d0-a119-78ecc0bb62cd'></a>

56

<a id='51950098-dfd4-4ea4-ad3b-0e38da91b44f'></a>

Figure 12: Credit card ROA and risk premium vs. corporate bond spreads

This figure presents Return on Assets (ROA) for borrowers' accounts (blue line), fitted ROA (black line) and estimated risk premium (purple line) from the two-stage approach of Fama and MacBeth (1973), transactor margin (orange dot) and default-adjusted spread of corporate bonds of different initial credit ratings (green, dotted line). A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Transactors are accounts that do not revolve a balance (i.e., are not borrowers). Borrower's ROA is the same as in Figure 8. To compute the risk premium and fitted ROA, we regress the ROA of borrower FICO portfolio i on its risk exposure, βi, using specification 2. The fitted ROA is defined as the predicted value of ROA based on the estimates from Equation 2 (λ̂ + ŷβ̂i). The risk premium corresponds to ŷβ̂i. Transactor margin is the average transactor ROA across all transactors (presented in Appendix Figure B6). Since transactors entail zero credit risk, we compare the transactor margin with the borrower portfolio at a FICO score of 850. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Transactors are accounts that do not revolve a balance (i.e., are not borrowers).
The default-adjusted spread for corporate bonds is estimated in two steps. First, using Mergent FISD on corporate bond issuances from 1990 to 2023, we form monthly portfolios of bond investments based on their date of issuance and initial credit rating. In the event of a bond default, we assume an average recovery rate of 40%, consistent with Standard & Poor's (S&P) estimates. Second, we compute the return on buy-and-hold-to-maturity rating portfolios. We adjust these returns for the risk-free return by subtracting the yield of a maturity-matched treasury as of the bond's issuance date. This gives us a monthly time series of default-adjusted credit spreads for each rating portfolio. The average of this time series is our estimate of the bond rating's default-adjusted credit spread. Second, to facilitate the comparison between bonds and credit cards, we map corporate bond ratings to FICO scores based on the 5-year expected default rates provided by S&P and our own calculations for credit cards.

<a id='54075cba-b1a8-4953-b4f4-db84b4e4a1a2'></a>

<::Line chart showing various financial metrics against FICO/ FICO Equivalent.

X-axis: FICO/ FICO Equivalent, ranging from 600 to 850.
Y-axis: Values from .01 to .11.

Legend:
- Fitted ROA (black line)
- Credit Card ROA (blue line)
- Bond Default Adjusted Spread (green dotted line with points labeled CCC/C, B, BB, BBB)
- Credit Card Risk Premium (purple line)

An additional label "transactor.margin" is present with an orange dot near the BBB point on the Bond Default Adjusted Spread line.
: chart::>

<a id='8d505937-58d9-4d9c-966a-690d44b10b96'></a>

57

<a id='b27c0c98-6455-49ac-b369-58d28d8bdc7c'></a>

Figure 13: Credit card ROA and the cost of regulatory capital

<a id='5f0efe5b-ca66-4dce-923c-2a998a446f3e'></a>

Panel (a) of this figure presents the regulatory risk weights implied by Basel III capital regulation for borrowers (blue line), transactors (green line), and all credit card accounts (red line), based on FICO scores at account origination. Accounts are grouped into 5-point FICO bins. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. A transactor is an account that does not revolve a balance (i.e., is not classified as a borrower). For borrowers and transactors within each FICO bin, we compute the account-level probability of default (PD) and loss given default (LGD) using Y-14 data, weighting the averages by Average Daily Balance (ADB). We then apply the formulas outlined in Section 5.1 to derive regulatory risk weights separately for borrowers and transactors. The risk weight for all accounts within a given FICO bin is calculated as the ADB-weighted average of borrower and transactor risk weights. Panel (b) compares the credit card ROA for all credit card accounts (blue line) with the implied cost of regulatory equity (red line). The credit card ROA follows the methodology used in Figure 8, except that it includes all accounts rather than only borrowers. The implied cost of regulatory equity is computed using the approach outlined in Section 5.1. This measure represents the return that credit card portfolios must generate to compensate for their higher risk weight while maintaining the same risk-weighted ROA as the average banking asset.

<a id='05547b81-ea26-4924-8b66-96cc8ff043c2'></a>

<::(a) Risk Weights by FICO: line chart::>FICO at Origination (x-axis) ranges from 600 to 850. Risk Weights (y-axis) ranges from 0.4 to 1.4. The chart shows three lines representing different groups: borrowers (blue line), transactors (red line), and all users (green line). The 'borrowers' line starts around 1.3 at FICO 600, peaks near 1.38, and then gradually decreases to approximately 0.75 at FICO 850. The 'transactors' line starts around 0.62 at FICO 600, decreases to about 0.45, and then remains relatively flat around 0.45-0.46 until FICO 850. The 'all users' line starts around 1.3 at FICO 600, peaks near 1.35, and then gradually decreases to approximately 0.6 at FICO 850. The 'all users' line generally falls between the 'borrowers' and 'transactors' lines. The lines generally show a decreasing trend in Risk Weights as FICO at Origination increases. The 'borrowers' and 'all users' lines show a more pronounced decrease than the 'transactors' line, which flattens out at higher FICO scores.

<a id='a1778893-448c-4e07-a27b-d1901cc9ffca'></a>

(b) ROA and Implied Cost of Regulatory Equity <::chart: A line chart titled "ROA and Implied Cost of Regulatory Equity". The y-axis is labeled "rate" and ranges from .01 to .11. The x-axis is labeled "FICO at Origination" and ranges from 600 to 850. Two lines are plotted: a blue line representing "Credit Card ROA" and a pink line representing "Implied cost of regulatory equity". The blue line starts around .105 at FICO 600, fluctuates slightly, drops sharply around FICO 650-660 to about .07, and then gradually declines to around .03 at FICO 840, with a slight increase at the very end. The pink line starts around .029 at FICO 600 and gradually declines to about .013 at FICO 850.::>

<a id='ba511683-1092-4295-bbe9-91ac2d11ab6e'></a>

58

<a id='109cefbb-288f-4d8e-b7c8-5627590af565'></a>

Tables

<a id='0b3ddb29-7a51-4e4c-bd2f-a6e5a25f37dc'></a>

Table 1
Summary statistics

<a id='3b053ea7-7b04-4cc5-b31d-8234467318c4'></a>

Panel A presents summary statistics for income and expense components at the bank-month level, based on Y-14 portfolio-level data from January 2015 until December 2023. The analysis is restricted to general-purpose consumer credit card portfolios. All variables are scaled by each bank's month-end balances and annualized. Panel B presents summary statistics for key balance, fee, and rate variables at the account level, specifically for accounts originated in January 2015 within our cleaned sample. Moments for fees, non-interest charge, charge-offs and recovery are computed only for observations where the corresponding variable has a non-zero value. All variables, except for rate variables, are reported in dollar amounts. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Active transactors are accounts that do not revolve a balance (i.e., are not borrowers) but remain active, meaning they exhibit a positive cycle-ending balance, purchase volume, or payment activity in a given month.

<a id='39ade8bb-e83e-4a83-8544-421b416a7e97'></a>

<table id="60-1">
<tr><td id="60-2"></td><td id="60-3" colspan="5">Panel A: Portfolio Level</td></tr>
<tr><td id="60-4"></td><td id="60-5">mean</td><td id="60-6">s.d.</td><td id="60-7"></td><td id="60-8">mean</td><td id="60-9">s.d.</td></tr>
<tr><td id="60-a">Interest</td><td id="60-b"></td><td id="60-c"></td><td id="60-d">Loss</td><td id="60-e"></td><td id="60-f"></td></tr>
<tr><td id="60-g">Interest Income</td><td id="60-h">0.142</td><td id="60-i">0.125</td><td id="60-j">Charge-off</td><td id="60-k">0.050</td><td id="60-l">0.023</td></tr>
<tr><td id="60-m">Interest Expense</td><td id="60-n">0.024</td><td id="60-o">0.022</td><td id="60-p">Recovery</td><td id="60-q">0.005</td><td id="60-r">0.004</td></tr>
<tr><td id="60-s">Non-Interest Income</td><td id="60-t" colspan="5">Non-Interest Expense</td></tr>
<tr><td id="60-u">Fee Income</td><td id="60-v">0.017</td><td id="60-w">0.015</td><td id="60-x">Reward</td><td id="60-y">0.048</td><td id="60-z">0.030</td></tr>
<tr><td id="60-A">Interchange</td><td id="60-B">0.071</td><td id="60-C">0.056</td><td id="60-D">Collection</td><td id="60-E">0.020</td><td id="60-F">0.010</td></tr>
<tr><td id="60-G">Other</td><td id="60-H">0.004</td><td id="60-I">0.008</td><td id="60-J">Fraud</td><td id="60-K">0.003</td><td id="60-L">0.002</td></tr>
<tr><td id="60-M"></td><td id="60-N"></td><td id="60-O"></td><td id="60-P">Other Operating</td><td id="60-Q">0.049</td><td id="60-R">0.078</td></tr>
<tr><td id="60-S"></td><td id="60-T" colspan="5">Panel B: Account Level</td></tr>
<tr><td id="60-U"></td><td id="60-V">N (millions)</td><td id="60-W">p25</td><td id="60-X">p50</td><td id="60-Y">p75</td><td id="60-Z">mean</td></tr>
<tr><td id="60-10" colspan="6">Borrowers</td></tr>
<tr><td id="60-11">ADB($)</td><td id="60-12">49.63</td><td id="60-13">805.59</td><td id="60-14">2058.78</td><td id="60-15">4382.68</td><td id="60-16">3340.33</td></tr>
<tr><td id="60-17">Purchase Volume ($)</td><td id="60-18">49.63</td><td id="60-19">0.00</td><td id="60-1a">50.72</td><td id="60-1b">392.82</td><td id="60-1c">507.28</td></tr>
<tr><td id="60-1d">Finance Charge ($)</td><td id="60-1e">49.63</td><td id="60-1f">4.03</td><td id="60-1g">24.49</td><td id="60-1h">62.32</td><td id="60-1i">45.43</td></tr>
<tr><td id="60-1j">Effective Interest Rate (%)</td><td id="60-1k">49.63</td><td id="60-1l">12.36</td><td id="60-1m">20.10</td><td id="60-1n">23.60</td><td id="60-1o">16.63</td></tr>
<tr><td id="60-1p">APR (%)</td><td id="60-1q">49.63</td><td id="60-1r">14.99</td><td id="60-1s">20.24</td><td id="60-1t">23.49</td><td id="60-1u">17.47</td></tr>
<tr><td id="60-1v">Credit Limit ($)</td><td id="60-1w">49.63</td><td id="60-1x">2300.00</td><td id="60-1y">5000.00</td><td id="60-1z">10000.00</td><td id="60-1A">7353.82</td></tr>
<tr><td id="60-1B">Late Fee ($)</td><td id="60-1C">5.88</td><td id="60-1D">25.00</td><td id="60-1E">35.00</td><td id="60-1F">37.00</td><td id="60-1G">28.39</td></tr>
<tr><td id="60-1H">Annual Fee ($)</td><td id="60-1I">0.97</td><td id="60-1J">39.00</td><td id="60-1K">49.01</td><td id="60-1L">95.00</td><td id="60-1M">67.10</td></tr>
<tr><td id="60-1N">Balance Transfer Fee ($)</td><td id="60-1O">0.31</td><td id="60-1P">139.30</td><td id="60-1Q">46.02</td><td id="60-1R">97.25</td><td id="60-1S">180.00</td></tr>
<tr><td id="60-1T">Total Non-interest Charge ($)</td><td id="60-1U">8.24</td><td id="60-1V">25.00</td><td id="60-1W">35.00</td><td id="60-1X">39.00</td><td id="60-1Y">37.25</td></tr>
<tr><td id="60-1Z">Charge-off (due to default)($)</td><td id="60-20">0.23</td><td id="60-21">942.96</td><td id="60-22">2392.02</td><td id="60-23">4845.04</td><td id="60-24">3722.04</td></tr>
<tr><td id="60-25">Charge-off (all reasons) ($)</td><td id="60-26">0.23</td><td id="60-27">941.99</td><td id="60-28">2391.02</td><td id="60-29">4843.18</td><td id="60-2a">3721.34</td></tr>
<tr><td id="60-2b">Recovery ($)</td><td id="60-2c">0.05</td><td id="60-2d">187.72</td><td id="60-2e">612.29</td><td id="60-2f">1750.00</td><td id="60-2g">1424.25</td></tr>
<tr><td id="60-2h" colspan="6">Active Transactors</td></tr>
<tr><td id="60-2i">ADB ($)</td><td id="60-2j">34.55</td><td id="60-2k">4.86</td><td id="60-2l">154.73</td><td id="60-2m">726.97</td><td id="60-2n">750.32</td></tr>
<tr><td id="60-2o">Purchase Volume ($)</td><td id="60-2p">34.55</td><td id="60-2q">58.00</td><td id="60-2r">411.16</td><td id="60-2s">1437.76</td><td id="60-2t">1312.33</td></tr>
<tr><td id="60-2u">APR (%)</td><td id="60-2v">34.55</td><td id="60-2w">14.24</td><td id="60-2x">16.99</td><td id="60-2y">20.99</td><td id="60-2z">16.35</td></tr>
<tr><td id="60-2A">Credit Limit ($)</td><td id="60-2B">34.55</td><td id="60-2C">4600.00</td><td id="60-2D">9000.00</td><td id="60-2E">15000.00</td><td id="60-2F">10895.47</td></tr>
<tr><td id="60-2G">Annual Fee ($)</td><td id="60-2H">0.84</td><td id="60-2I">39.00</td><td id="60-2J">75.00</td><td id="60-2K">95.00</td><td id="60-2L">80.29</td></tr>
<tr><td id="60-2M">Total Non-interest Charge ($)</td><td id="60-2N">1.55</td><td id="60-2O">2.91</td><td id="60-2P">39.00</td><td id="60-2Q">94.68</td><td id="60-2R">49.32</td></tr>
</table>

<a id='4a480713-f4c9-4067-8619-23337395fb47'></a>

59

<a id='3552b3a2-74cd-4c59-b512-e2dd93b35639'></a>

Table 2

<a id='b1dd2b01-ecee-4301-a1cb-a33df151dd6c'></a>

Profit components by account type and origination FICO score

<a id='9959363d-12d4-4051-9687-6e1543fa87b3'></a>

This table presents the breakdown of profit components by origination FICO bins, grouped in 20-point increments, separately for borrowers, transactors, and all users, for accounts originated between January 2015 and December 2017. ADB share represents the proportion of lifetime Average Daily Balance (ADB) contributed by accounts within a given FICO bin relative to the total ADB for each user group. All average rate variables are constructed using the same methodology as in Figure 8: for each origination FICO bin, we compute the cumulative monthly dollar amount of the variable of interest across all accounts in that bin over their lifetime, then divide by their cumulative ADB. Variable definitions are provided in Section 4. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Active transactors are accounts that do not revolve a balance (i.e., are not borrowers) but remain active, meaning they exhibit a positive cycle-ending balance, purchase volume, or payment activity in a given month. All rates are annualized.

<a id='8327f212-024b-40a0-8c29-6e4966bbdc7f'></a>

<table id="61-1">
<tr><td id="61-2">Origination FICO</td><td id="61-3">ADB Share (%)</td><td id="61-4">Interest Spread (%)</td><td id="61-5">Net Charge-off (%)</td><td id="61-6">Interchange (%)</td><td id="61-7">Reward (%)</td><td id="61-8">Fee (%)</td><td id="61-9">Operating Expense (%)</td><td id="61-a">ROA (%)</td></tr>
<tr><td id="61-b" colspan="9">Panel A: Borrowers</td></tr>
<tr><td id="61-c">00</td><td id="61-d">1.30</td><td id="61-e">21.28</td><td id="61-f">9.35</td><td id="61-g">2.91</td><td id="61-h">2.15</td><td id="61-i">5.13</td><td id="61-j">7.52</td><td id="61-k">10.64</td></tr>
<tr><td id="61-l">620</td><td id="61-m">2.71</td><td id="61-n">20.44</td><td id="61-o">8.92</td><td id="61-p">2.69</td><td id="61-q">2.15</td><td id="61-r">4.36</td><td id="61-s">6.35</td><td id="61-t">10.41</td></tr>
<tr><td id="61-u">640</td><td id="61-v">5.34</td><td id="61-w">19.84</td><td id="61-x">8.06</td><td id="61-y">2.53</td><td id="61-z">2.09</td><td id="61-A">3.68</td><td id="61-B">5.55</td><td id="61-C">10.71</td></tr>
<tr><td id="61-D">660</td><td id="61-E">8.89</td><td id="61-F">18.45</td><td id="61-G">7.43</td><td id="61-H">2.39</td><td id="61-I">2.00</td><td id="61-J">2.87</td><td id="61-K">5.19</td><td id="61-L">9.35</td></tr>
<tr><td id="61-M">680</td><td id="61-N">14.38</td><td id="61-O">16.62</td><td id="61-P">7.09</td><td id="61-Q">2.28</td><td id="61-R">1.90</td><td id="61-S">2.17</td><td id="61-T">4.97</td><td id="61-U">7.24</td></tr>
<tr><td id="61-V">700</td><td id="61-W">14.62</td><td id="61-X">15.55</td><td id="61-Y">6.41</td><td id="61-Z">2.45</td><td id="61-10">2.07</td><td id="61-11">1.99</td><td id="61-12">4.86</td><td id="61-13">6.76</td></tr>
<tr><td id="61-14">720</td><td id="61-15">13.48</td><td id="61-16">14.32</td><td id="61-17">5.72</td><td id="61-18">2.69</td><td id="61-19">2.31</td><td id="61-1a">1.92</td><td id="61-1b">4.70</td><td id="61-1c">6.28</td></tr>
<tr><td id="61-1d">740</td><td id="61-1e">11.66</td><td id="61-1f">13.14</td><td id="61-1g">5.04</td><td id="61-1h">3.01</td><td id="61-1i">2.63</td><td id="61-1j">1.89</td><td id="61-1k">4.60</td><td id="61-1l">5.84</td></tr>
<tr><td id="61-1m">760</td><td id="61-1n">9.43</td><td id="61-1o">11.96</td><td id="61-1p">4.43</td><td id="61-1q">3.46</td><td id="61-1r">3.05</td><td id="61-1s">1.91</td><td id="61-1t">4.53</td><td id="61-1u">5.37</td></tr>
<tr><td id="61-1v">780</td><td id="61-1w">7.17</td><td id="61-1x">10.86</td><td id="61-1y">3.82</td><td id="61-1z">4.17</td><td id="61-1A">3.69</td><td id="61-1B">2.01</td><td id="61-1C">4.50</td><td id="61-1D">5.08</td></tr>
<tr><td id="61-1E">800</td><td id="61-1F">5.31</td><td id="61-1G">9.72</td><td id="61-1H">3.17</td><td id="61-1I">5.10</td><td id="61-1J">4.54</td><td id="61-1K">2.16</td><td id="61-1L">4.46</td><td id="61-1M">4.84</td></tr>
<tr><td id="61-1N">820</td><td id="61-1O">3.43</td><td id="61-1P">8.74</td><td id="61-1Q">2.45</td><td id="61-1R">6.01</td><td id="61-1S">5.59</td><td id="61-1T">2.44</td><td id="61-1U">4.21</td><td id="61-1V">4.98</td></tr>
<tr><td id="61-1W">840</td><td id="61-1X">1.90</td><td id="61-1Y">7.77</td><td id="61-1Z">1.65</td><td id="61-20">6.90</td><td id="61-21">6.81</td><td id="61-22">2.68</td><td id="61-23">3.95</td><td id="61-24">4.98</td></tr>
<tr><td id="61-25">850</td><td id="61-26">0.39</td><td id="61-27">7.22</td><td id="61-28">1.27</td><td id="61-29">7.55</td><td id="61-2a">7.40</td><td id="61-2b">2.86</td><td id="61-2c">3.95</td><td id="61-2d">5.05</td></tr>
<tr><td id="61-2e" colspan="2">Average (ADB-weighted)</td><td id="61-2f">14.55</td><td id="61-2g">5.75</td><td id="61-2h">3.12</td><td id="61-2i">2.72</td><td id="61-2j">2.31</td><td id="61-2k">4.84</td><td id="61-2l">6.79</td></tr>
<tr><td id="61-2m" colspan="9">Panel B: Transactors</td></tr>
<tr><td id="61-2n">6600</td><td id="61-2o">0.3</td><td id="61-2p"></td><td id="61-2q"></td><td id="61-2r">54.56</td><td id="61-2s">41.45</td><td id="61-2t">14.09</td><td id="61-2u">6.91</td><td id="61-2v">16.43</td></tr>
<tr><td id="61-2w">620</td><td id="61-2x">0.71</td><td id="61-2y"></td><td id="61-2z"></td><td id="61-2A">50.59</td><td id="61-2B">41.66</td><td id="61-2C">10.29</td><td id="61-2D">5.62</td><td id="61-2E">9.22</td></tr>
<tr><td id="61-2F">640</td><td id="61-2G">1.46</td><td id="61-2H"></td><td id="61-2I"></td><td id="61-2J">49.14</td><td id="61-2K">41.68</td><td id="61-2L">8.55</td><td id="61-2M">4.85</td><td id="61-2N">6.68</td></tr>
<tr><td id="61-2O">660</td><td id="61-2P">2.57</td><td id="61-2Q"></td><td id="61-2R"></td><td id="61-2S">46.99</td><td id="61-2T">40.10</td><td id="61-2U">6.62</td><td id="61-2V">4.58</td><td id="61-2W">4.39</td></tr>
<tr><td id="61-2X">680</td><td id="61-2Y">4.35</td><td id="61-2Z"></td><td id="61-30"></td><td id="61-31">44.56</td><td id="61-32">37.77</td><td id="61-33">5.16</td><td id="61-34">4.50</td><td id="61-35">2.89</td></tr>
<tr><td id="61-36">700</td><td id="61-37">5.79</td><td id="61-38"></td><td id="61-39"></td><td id="61-3a">43.29</td><td id="61-3b">37.11</td><td id="61-3c">4.89</td><td id="61-3d">4.38</td><td id="61-3e">2.70</td></tr>
<tr><td id="61-3f">720</td><td id="61-3g">7.29</td><td id="61-3h"></td><td id="61-3i"></td><td id="61-3j">42.19</td><td id="61-3k">36.68</td><td id="61-3l">5.15</td><td id="61-3m">4.25</td><td id="61-3n">2.89</td></tr>
<tr><td id="61-3o">740</td><td id="61-3p">8.88</td><td id="61-3q"></td><td id="61-3r"></td><td id="61-3s">40.96</td><td id="61-3t">36.24</td><td id="61-3u">5.29</td><td id="61-3v">4.12</td><td id="61-3w">2.77</td></tr>
<tr><td id="61-3x">760</td><td id="61-3y">10.39</td><td id="61-3z"></td><td id="61-3A"></td><td id="61-3B">39.93</td><td id="61-3C">35.30</td><td id="61-3D">5.24</td><td id="61-3E">4.17</td><td id="61-3F">2.87</td></tr>
<tr><td id="61-3G">780</td><td id="61-3H">12.74</td><td id="61-3I"></td><td id="61-3J"></td><td id="61-3K">39.12</td><td id="61-3L">34.06</td><td id="61-3M">4.84</td><td id="61-3N">4.32</td><td id="61-3O">3.01</td></tr>
<tr><td id="61-3P">800</td><td id="61-3Q">16.32</td><td id="61-3R"></td><td id="61-3S"></td><td id="61-3T">38.37</td><td id="61-3U">32.66</td><td id="61-3V">4.33</td><td id="61-3W">4.48</td><td id="61-3X">3.21</td></tr>
<tr><td id="61-3Y">820</td><td id="61-3Z">15.48</td><td id="61-40"></td><td id="61-41"></td><td id="61-42">35.39</td><td id="61-43">31.61</td><td id="61-44">4.48</td><td id="61-45">3.99</td><td id="61-46">2.01</td></tr>
<tr><td id="61-47">840</td><td id="61-48">10.9</td><td id="61-49"></td><td id="61-4a"></td><td id="61-4b">31.53</td><td id="61-4c">30.57</td><td id="61-4d">4.7</td><td id="61-4e">3.57</td><td id="61-4f">0.16</td></tr>
<tr><td id="61-4g">850</td><td id="61-4h">2.83</td><td id="61-4i"></td><td id="61-4j"></td><td id="61-4k">31.41</td><td id="61-4l">30.04</td><td id="61-4m">4.68</td><td id="61-4n">3.55</td><td id="61-4o">0.29</td></tr>
<tr><td id="61-4p" colspan="2">Average (ADB-weighted)</td><td id="61-4q"></td><td id="61-4r"></td><td id="61-4s">38.8</td><td id="61-4t">34.15</td><td id="61-4u">4.97</td><td id="61-4v">4.2</td><td id="61-4w">2.57</td></tr>
<tr><td id="61-4x" colspan="9">Panel C: All Users</td></tr>
<tr><td id="61-4y">600</td><td id="61-4z">1.18</td><td id="61-4A">20.48</td><td id="61-4B">9.03</td><td id="61-4C">4.66</td><td id="61-4D">3.46</td><td id="61-4E">5.43</td><td id="61-4F">7.50</td><td id="61-4G">10.82</td></tr>
<tr><td id="61-4H">620</td><td id="61-4I">2.45</td><td id="61-4J">19.59</td><td id="61-4K">8.59</td><td id="61-4L">4.52</td><td id="61-4M">3.61</td><td id="61-4N">4.58</td><td id="61-4O">6.32</td><td id="61-4P">10.37</td></tr>
<tr><td id="61-4Q">640</td><td id="61-4R">4.84</td><td id="61-4S">18.96</td><td id="61-4T">7.74</td><td id="61-4U">4.41</td><td id="61-4V">3.63</td><td id="61-4W">3.87</td><td id="61-4X">5.53</td><td id="61-4Y">10.55</td></tr>
<tr><td id="61-4Z">660</td><td id="61-50">8.08</td><td id="61-51">17.58</td><td id="61-52">7.13</td><td id="61-53">4.30</td><td id="61-54">3.56</td><td id="61-55">3.02</td><td id="61-56">5.17</td><td id="61-57">9.14</td></tr>
<tr><td id="61-58">680</td><td id="61-59">13.09</td><td id="61-5a">15.79</td><td id="61-5b">6.79</td><td id="61-5c">4.16</td><td id="61-5d">3.44</td><td id="61-5e">2.30</td><td id="61-5f">4.95</td><td id="61-5g">7.05</td></tr>
<tr><td id="61-5h">700</td><td id="61-5i">13.48</td><td id="61-5j">14.55</td><td id="61-5k">6.05</td><td id="61-5l">4.80</td><td id="61-5m">4.01</td><td id="61-5n">2.15</td><td id="61-5o">4.83</td><td id="61-5p">6.53</td></tr>
<tr><td id="61-5q">720</td><td id="61-5r">12.69</td><td id="61-5s">13.09</td><td id="61-5t">5.30</td><td id="61-5u">5.70</td><td id="61-5v">4.85</td><td id="61-5w">2.16</td><td id="61-5x">4.67</td><td id="61-5y">6.02</td></tr>
<tr><td id="61-5z">740</td><td id="61-5A">11.30</td><td id="61-5B">11.60</td><td id="61-5C">4.53</td><td id="61-5D">6.95</td><td id="61-5E">6.03</td><td id="61-5F">2.24</td><td id="61-5G">4.55</td><td id="61-5H">5.53</td></tr>
<tr><td id="61-5I">760</td><td id="61-5J">9.55</td><td id="61-5K">10.00</td><td id="61-5L">3.81</td><td id="61-5M">8.67</td><td id="61-5N">7.56</td><td id="61-5O">2.38</td><td id="61-5P">4.48</td><td id="61-5Q">5.02</td></tr>
<tr><td id="61-5R">780</td><td id="61-5S">7.88</td><td id="61-5T">8.19</td><td id="61-5U">3.03</td><td id="61-5V">11.55</td><td id="61-5W">10.00</td><td id="61-5X">2.59</td><td id="61-5Y">4.46</td><td id="61-5Z">4.64</td></tr>
<tr><td id="61-60">800</td><td id="61-61">6.73</td><td id="61-62">6.08</td><td id="61-63">2.18</td><td id="61-64">15.61</td><td id="61-65">13.31</td><td id="61-66">2.83</td><td id="61-67">4.47</td><td id="61-68">4.33</td></tr>
<tr><td id="61-69">820</td><td id="61-6a">4.98</td><td id="61-6b">4.48</td><td id="61-6c">1.47</td><td id="61-6d">17.89</td><td id="61-6e">15.98</td><td id="61-6f">3.25</td><td id="61-6g">4.12</td><td id="61-6h">3.78</td></tr>
<tr><td id="61-6i">840</td><td id="61-6j">3.06</td><td id="61-6k">3.32</td><td id="61-6l">0.89</td><td id="61-6m">18.32</td><td id="61-6n">17.70</td><td id="61-6o">3.61</td><td id="61-6p">3.78</td><td id="61-6q">2.60</td></tr>
<tr><td id="61-6r">850</td><td id="61-6s">0.70</td><td id="61-6t">2.48</td><td id="61-6u">0.61</td><td id="61-6v">2003</td><td id="61-6w">19.13</td><td id="61-6x">3.80</td><td id="61-6y">3.75</td><td id="61-6z">2.56</td></tr>
<tr><td id="61-6A" colspan="2">Average (ADB-weighted)</td><td id="61-6B">12.41</td><td id="61-6C">5.01</td><td id="61-6D">7.81</td><td id="61-6E">6.76</td><td id="61-6F">2.65</td><td id="61-6G">4.76</td><td id="61-6H">6.24</td></tr>
</table>

<a id='19353e24-c65d-42aa-950d-adf1c35cc320'></a>

Table 3
Credit card profit components and bank operating expenses

<a id='1b992c62-2d9e-4de8-af24-1857eaceb4bd'></a>

This table presents regressions of interest spread, net charge-off rate, and gross margin on the operating expense rate. Observations are aggregated at the bank-origination FICO bin level from account-level data. Interest spread is defined as the sum of finance charge less interest expense across all borrower observations in a bank-origination FICO bin, then divided the total borrower Average Daily Balance (ADB) in that bin. Similarly, the net charge-off rate is calculated as total charge-offs minus recoveries divided by the bin's total ADB, and gross margin is computed as total gross profit over total ADB. The operating expense rate is measured at the bank-month level and averaged across time for each bank. Regressions are weighted by ADB of the FICO bin, and standard errors in parentheses are clustered at the bank level. *** p<0.01, ** p<0.05, * p<0.1

<a id='e1855733-274b-49c0-a339-5d78f20eb5ca'></a>

<table id="62-1">
<tr><td id="62-2"></td><td id="62-3">Interest Spread</td><td id="62-4">Net Charge-off</td><td id="62-5">Gross Margin</td></tr>
<tr><td id="62-6"></td><td id="62-7">(1)</td><td id="62-8">(2)</td><td id="62-9">(3)</td></tr>
<tr><td id="62-a">Operating Expense</td><td id="62-b">0.622***</td><td id="62-c">0.139</td><td id="62-d">1.127**</td></tr>
<tr><td id="62-e"></td><td id="62-f">(0.119)</td><td id="62-g">(0.149)</td><td id="62-h">(0.528)</td></tr>
<tr><td id="62-i">Constant</td><td id="62-j">0.114***</td><td id="62-k">0.043***</td><td id="62-l">0.055**</td></tr>
<tr><td id="62-m"></td><td id="62-n">(0.008)</td><td id="62-o">(0.007)</td><td id="62-p">(0.020)</td></tr>
<tr><td id="62-q">Origination FICO FE</td><td id="62-r">Y</td><td id="62-s">Y</td><td id="62-t">Y</td></tr>
<tr><td id="62-u">Observations</td><td id="62-v">919</td><td id="62-w">908</td><td id="62-x">908</td></tr>
<tr><td id="62-y">R2</td><td id="62-z">0.895</td><td id="62-A">0.734</td><td id="62-B">0.489</td></tr>
</table>

<a id='d6eb5edf-777b-437d-bbb5-3f08fa73cd69'></a>

61

<a id='dd8d2d2f-9e3b-4583-a620-6afa8069205c'></a>

Table 4

<a id='6358314b-cd93-438e-8787-ecae75f4785b'></a>

Risk premium estimates by origination FICO score

<a id='e765d2ad-090c-4573-be40-7ecda814ffb1'></a>

This table presents estimates of the risk exposure for each FICO score bin portfolio using the two-stage approach of Fama and MacBeth (1973). We first estimate a single-factor model of default risk using the cross-section of credit card portfolios. We use the monthly change in the aggregate credit card portfolio's charge-off rate as a proxy for the systematic component of default risk. For each FICO portfolio i, we estimate its beta to systematic default risk by regressing the change in its monthly charge-off rate on the change in the charge-off rate of the aggregate credit card portfolio following Equation 1. Second, we use the FICO-specific risk exposures, ß, from the first stage to estimate the compensation for default-risk exposure and the corresponding risk premium. To this end, we regress the ROA of FICO portfolio i on its risk exposure, ßi, using specification 2. Fitted ROA is defined as the predicted value of ROA using the estimates from Equation 2 (λ+βιγ). Risk premium corresponds to βιγ. We define risk-adjusted ROA as the difference between ROA and the risk premium. We compute standard errors using the Newey-West correction with an optimal number of lags to account for potential autocorrelation and heteroskedasticity in the residuals. Adjusted standard errors are reported in parentheses. *** p<0.01, ** p<0.05, * p<0.1

<a id='f0f78ad2-59b6-49cf-b53f-3beeba7dba87'></a>

<table id="63-1">
<tr><td id="63-2">Parameter Estimates</td><td id="63-3">γ 0.0526***</td><td id="63-4">λ 0.0241*** (0.0065)</td><td id="63-5"></td><td id="63-6"></td><td id="63-7"></td></tr>
<tr><td id="63-8">Origination FICO</td><td id="63-9">β</td><td id="63-a">ROA</td><td id="63-b">Fitted ROA</td><td id="63-c">Risk Premium</td><td id="63-d">Risk-adj. ROA</td></tr>
<tr><td id="63-e">600</td><td id="63-f">1.628</td><td id="63-g">10.61%</td><td id="63-h">10.98%</td><td id="63-i">8.56%</td><td id="63-j">2.05%</td></tr>
<tr><td id="63-k"></td><td id="63-l">(0.235)</td><td id="63-m"></td><td id="63-n">(1.04%)</td><td id="63-o">(0.73%)</td><td id="63-p">(0.73%)</td></tr>
<tr><td id="63-q">620</td><td id="63-r">1.609</td><td id="63-s">10.53%</td><td id="63-t">10.87%</td><td id="63-u">8.46%</td><td id="63-v">2.07%</td></tr>
<tr><td id="63-w"></td><td id="63-x">(0.172)</td><td id="63-y"></td><td id="63-z">(1.03%)</td><td id="63-A">(0.72%)</td><td id="63-B">(0.72%)</td></tr>
<tr><td id="63-C">640</td><td id="63-D">1.327</td><td id="63-E">10.80%</td><td id="63-F">9.39%</td><td id="63-G">6.98%</td><td id="63-H">3.82%</td></tr>
<tr><td id="63-I"></td><td id="63-J">(0.109)</td><td id="63-K"></td><td id="63-L">(0.94%)</td><td id="63-M">(0.59%)</td><td id="63-N">(0.59%)</td></tr>
<tr><td id="63-O">660</td><td id="63-P">1.324</td><td id="63-Q">9.41%</td><td id="63-R">9.38%</td><td id="63-S">6.96%</td><td id="63-T">2.45%</td></tr>
<tr><td id="63-U"></td><td id="63-V">(0.079)</td><td id="63-W"></td><td id="63-X">(0.93%)</td><td id="63-Y">(0.59%)</td><td id="63-Z">(0.59%)</td></tr>
<tr><td id="63-10">680</td><td id="63-11">1.222</td><td id="63-12">7.30%</td><td id="63-13">8.84%</td><td id="63-14">6.43%</td><td id="63-15">0.87%</td></tr>
<tr><td id="63-16"></td><td id="63-17">(0.077)</td><td id="63-18"></td><td id="63-19">(0.90%)</td><td id="63-1a">(0.55%)</td><td id="63-1b">(0.55%)</td></tr>
<tr><td id="63-1c">700</td><td id="63-1d">0.987</td><td id="63-1e">6.81%</td><td id="63-1f">7.61%</td><td id="63-1g">5.19%</td><td id="63-1h">1.61%</td></tr>
<tr><td id="63-1i"></td><td id="63-1j">(0.065)</td><td id="63-1k"></td><td id="63-1l">(0.83%)</td><td id="63-1m">(0.44%)</td><td id="63-1n">(0.44%)</td></tr>
<tr><td id="63-1o">720</td><td id="63-1p">1.012</td><td id="63-1q">6.30%</td><td id="63-1r">7.74%</td><td id="63-1s">5.32%</td><td id="63-1t">0.98%</td></tr>
<tr><td id="63-1u"></td><td id="63-1v">(0.079)</td><td id="63-1w"></td><td id="63-1x">(0.84%)</td><td id="63-1y">(0.45%)</td><td id="63-1z">(0.45%)</td></tr>
<tr><td id="63-1A">740</td><td id="63-1B">0.833</td><td id="63-1C">5.86%</td><td id="63-1D">6.79%</td><td id="63-1E">4.38%</td><td id="63-1F">1.47%</td></tr>
<tr><td id="63-1G"></td><td id="63-1H">(0.112)</td><td id="63-1I"></td><td id="63-1J">(0.79%)</td><td id="63-1K">(0.37%)</td><td id="63-1L">(0.37%)</td></tr>
<tr><td id="63-1M">760</td><td id="63-1N">0.751</td><td id="63-1O">5.37%</td><td id="63-1P">6.36%</td><td id="63-1Q">3.95%</td><td id="63-1R">1.42%</td></tr>
<tr><td id="63-1S"></td><td id="63-1T">(0.121)</td><td id="63-1U"></td><td id="63-1V">(0.77%)</td><td id="63-1W">(0.34%)</td><td id="63-1X">(0.34%)</td></tr>
<tr><td id="63-1Y">780</td><td id="63-1Z">0.610</td><td id="63-20">5.06%</td><td id="63-21">5.62%</td><td id="63-22">3.21%</td><td id="63-23">1.85%</td></tr>
<tr><td id="63-24"></td><td id="63-25">(0.116)</td><td id="63-26"></td><td id="63-27">(0.74%)</td><td id="63-28">(0.27%)</td><td id="63-29">(0.27%)</td></tr>
<tr><td id="63-2a">800</td><td id="63-2b">0.464</td><td id="63-2c">4.81%</td><td id="63-2d">4.86%</td><td id="63-2e">2.44%</td><td id="63-2f">2.37%</td></tr>
<tr><td id="63-2g"></td><td id="63-2h">(0.144)</td><td id="63-2i"></td><td id="63-2j">(0.71%)</td><td id="63-2k">(0.21%)</td><td id="63-2l">(0.21%)</td></tr>
<tr><td id="63-2m">820</td><td id="63-2n">0.326</td><td id="63-2o">4.94%</td><td id="63-2p">4.13%</td><td id="63-2q">1.71%</td><td id="63-2r">3.23%</td></tr>
<tr><td id="63-2s"></td><td id="63-2t">(0.122)</td><td id="63-2u"></td><td id="63-2v">(0.69%)</td><td id="63-2w">(0.15%)</td><td id="63-2x">(0.15%)</td></tr>
<tr><td id="63-2y">840</td><td id="63-2z">0.333</td><td id="63-2A">4.97%</td><td id="63-2B">4.17%</td><td id="63-2C">1.75%</td><td id="63-2D">3.22%</td></tr>
<tr><td id="63-2E"></td><td id="63-2F">(0.154)</td><td id="63-2G"></td><td id="63-2H">(0.69%)</td><td id="63-2I">(0.15%)</td><td id="63-2J">(0.15%)</td></tr>
<tr><td id="63-2K">850</td><td id="63-2L">0.338</td><td id="63-2M">5.05%</td><td id="63-2N">4.19%</td><td id="63-2O">1.78%</td><td id="63-2P">3.28%</td></tr>
<tr><td id="63-2Q"></td><td id="63-2R">(0.152)</td><td id="63-2S"></td><td id="63-2T">(0.69%) 62</td><td id="63-2U">(0.15%)</td><td id="63-2V">(0.15%)</td></tr>
</table>
02

<a id='79a0b18e-5167-4f2c-9415-9a8e3af1bac3'></a>

Appendix

<a id='0110fb8d-8ab8-4d05-8f3f-cf1d8efe1e7e'></a>

A Variable Definition

<a id='4f19acbb-0ada-460c-9896-80ec0873f1c5'></a>

A.1 Interchange Rate and Rewards Rate

Interchange fees and rewards expenses are both dollar amounts in portfolio-level data, and portfolio-level data only has total balances of credit cards but not purchase volumes. To estimate their rates as a percentage of purchase volume, we did the following steps. First, we compute the total amount of purchase volumes of rewards cards and total amount of purchase volumes for both rewards and classic cards for each bank in each month from the account-level data. Next, we merge the two purchase volumes to portfolio-level data. To compute the rewards rate, we divide the amounts of reward expenses by the amounts of purchase volumes of rewards cards. We examine each bank's reward rates one by one by plotting their time-series graphs and find that there are still some outliers for certain banks and certain months. We remove the effect of outliers by (1) dropping banks whose median rewards rates are higher than 5% (2) dropping bank-month observations whose rewards rates are higher than 5% or are negative (3) dropping six small card issuers who have unreasonable levels of reward rates (overall very high and jump up and down from one month to next month), and those banks also have very short sample periods (e.g. only two years of data). The 5% cutoff point is already very conservative since it is a very high number for an average rewards rate across millions of different accounts. To compute the interchange rate, we divide the amounts of interchange fees by the amounts of purchase volume of all cards. Afterwards, we smooth both reward rates and interchange rates by taking their 12-month moving averages. The average interchange (reward) rate as a share of purchase volume in our data is around 1.9% (1.4%). Then we merge the interchange rates and reward rates obtained from the portfolio-level data to the account-level data at the bank-month level.

<a id='746e8b20-4372-49d0-b1e2-da6df901efb3'></a>

63

<a id='86fa9bcc-3a80-4106-8277-38435f9fd4eb'></a>

For accounts that have missing values of interchange or reward rates (e.g. accounts from the 6 banks we dropped when computing reward rates in portfolio-level data), we fill in the missing values by taking the median rates across all banks within each month. Finally, we obtain the dollar amount of interchange fees and rewards for each account in each month by multiplying their associated interchange rates and reward rates with purchase volumes. The total amount of interchange income and rewards expenses for all credit card issuers in 2023 were US$75 billion and US$65 billion, respectively.

<a id='ea944105-102e-487e-a025-63acb980dcf6'></a>

64

<a id='5258dad2-e2b8-441e-9fab-20f9ddd516ec'></a>

B

<a id='879206f0-6a01-4228-aa3e-fc2289a58584'></a>

# Appendix Figures

<a id='c0816c9f-e043-4418-a582-e2998a10f719'></a>

Figure B1: Fee income

Panel (a) shows how non-interest fees evolve over accounts' lifetime, separately for accounts with origination FICO scores of 605, 655, 705, 755, and 805. The non-interest fee is defined as the sum of balance transfer fees, late fees, annual/monthly fees, cash advance fees, non-sufficient fund fees, and other non-interest charges. At each month of account age, the total non-interest income for each FICO bin is divided by the total Average Daily Balance (ADB) to compute the fee ratio. Panel (b) plots the lifetime average fee income rate for accounts grouped by origination FICO scores. For each FICO bin, we calculate the cumulative lifetime dollar amount of non-interest fees and divide it by the lifetime ADB. The resulting rate is then annualized.
(a) Fee income over account's lifetime

<a id='1852e7f3-f0e2-42dd-a392-529c5b0d25cd'></a>

<::Line chart titled "Non-interest Fees as Share of ADB". The y-axis is labeled "Non-interest Fees as Share of ADB" and ranges from 0 to 0.06. The x-axis is labeled "Months since Account Origination" and ranges from 0 to 80. There are five lines on the chart, each representing a different value as indicated by the legend:
- 605 (blue line)
- 655 (red line)
- 705 (green line)
- 755 (yellow line)
- 805 (purple line)

All lines show a general decreasing trend with periodic spikes occurring approximately every 12 months. The blue line (605) starts highest, around 0.058, and has the most pronounced spikes, reaching up to 0.018. The other lines start lower and have smaller spikes.::>

<a id='51d79dcc-1bab-471c-a090-0cdf3e6ba344'></a>

<::Line chart titled "(b) Average fee income by origination FICO score". The y-axis is labeled "Share of Lifetime ADB" and ranges from .02 to .16. The x-axis is labeled "FICO at Account Origination" and ranges from 600 to 850. There are two lines plotted: a blue line representing "Borrowers" and a red line representing "Transactors". The red line (Transactors) starts around .145 at FICO 600, decreases sharply to around .08 at FICO 670, then fluctuates between .04 and .055, ending around .045 at FICO 850. The blue line (Borrowers) starts around .05 at FICO 600, decreases to around .02 at FICO 700, and then gradually increases to around .03 at FICO 850.: chart::>

<a id='e8ad118a-0b4f-45af-8c12-decd212f82b4'></a>

65

<a id='9375455a-0420-4d36-97c7-bdd80a235ee7'></a>

Figure B2: Gross margin

This figure presents all non-operating income and expense components (all on the left y-axis) along with gross margin (black line on the right y-axis) for borrowers and all accounts, grouped by FICO scores at account origination. A borrower is defined as an account that either revolves a balance (fails to repay the full balance within the grace period) or is charged off in a given month. Income components are plotted as positive values, while losses and expenses appear as negative values. Interest income, interest expense and credit loss are computed as in Figure 4. Non-interest income includes interchange income as computed in Figure 6b plus fee income. Non-interest expense includes rewards income in Figure 6b, interchange expenses and fraud. All lifetime average rate variables are constructed following the methodology in Section 4: for each origination FICO bin, we compute the cumulative lifetime dollar amount of each component across all accounts in the bin over the entire sample period, then divide it by their cumulative Average Daily Balance (ADB). Gross margin is defined as interest spread minus net charge-offs, plus net interchange income (interchange minus rewards), plus the fee income rate, minus other non-operating expenses. All rates are annualized.

<a id='0aff96c1-0a9f-4d3c-babf-39d9b1f3f8df'></a>

(a) Borrowers <::Stacked area chart with an overlaid line graph titled "(a) Borrowers". The x-axis is "FICO at Account Origination" ranging from 600 to 850. The left y-axis is "Share of Lifetime ADB" ranging from -0.15 to 0.3. The right y-axis is "Gross Margin" ranging from 0.09 to 0.19. The chart shows five stacked areas and one line: Interest Income (blue area) decreases from approximately 0.25 to 0.1, Non-Interest Income (yellow area) decreases from approximately 0.05 to 0.03, Interest Expense (red area) is a thin band around 0, Credit Loss (green area) decreases from approximately -0.05 to -0.01, and Non-Interest Expense (purple area) increases from approximately -0.08 to -0.12. The Gross Margin (black line, right axis) starts at approximately 0.19 at FICO 600, drops sharply to around 0.12 at FICO 675, and then gradually declines to approximately 0.09 at FICO 850. The legend below the chart indicates: Interest Income (blue), Credit Loss (green), Non-Interest Income (yellow), Non-Interest Expense (purple), Interest Expense (red), and Gross Margin (black line, right axis).: chart::> (b) All Users <::Stacked area chart with an overlaid line graph titled "(b) All Users". The x-axis is "FICO at Account Origination" ranging from 600 to 850. The left y-axis is "Share of Lifetime ADB" ranging from -0.2 to 0.3. The right y-axis is "Gross Margin" ranging from 0.06 to 0.2. The chart shows five stacked areas and one line: Interest Income (blue area) decreases from approximately 0.25 to 0.1, Non-Interest Income (yellow area) decreases from approximately 0.05 to 0.03, Interest Expense (red area) is a thin band around 0, Credit Loss (green area) decreases from approximately -0.08 to -0.02, and Non-Interest Expense (purple area) increases from approximately -0.12 to -0.18. The Gross Margin (black line, right axis) starts at approximately 0.19 at FICO 600, drops sharply to around 0.12 at FICO 675, and then gradually declines to approximately 0.06 at FICO 850. The legend below the chart indicates: Interest Income (blue), Credit Loss (green), Non-Interest Income (yellow), Non-Interest Expense (purple), Interest Expense (red), and Gross Margin (black line, right axis).: chart::>

<a id='5a890295-365a-4e1a-a6d4-53b6c9f95777'></a>

66

<a id='15673feb-3186-42c2-b313-81b64597c60d'></a>

Figure B3: Operating expense example: Capital One

Panel (a) is a screenshot from Capital One's 2023 Annual Report Table 4. It displays the components of bank's non-interest expense for 2023. Panel (b) is a screenshot of Table 8 from Capital One's 2023 annual report. It summarizes the financial results of Capital One's credit card business and displays selected key metrics for the periods indicated.
(a) Bank Level Non-Interest Expense

<a id='229e5d8a-2faf-4792-877c-99535c83fcc3'></a>

<table id="68-1">
<tr><td id="68-2"></td><td id="68-3">Year</td></tr>
<tr><td id="68-4">(Dollars in millions)</td><td id="68-5">2023</td></tr>
<tr><td id="68-6">Operating Expense:</td><td id="68-7"></td></tr>
<tr><td id="68-8">Salaries and associate benefits(1)</td><td id="68-9">$ 9,302</td></tr>
<tr><td id="68-a">Occupancy and equipment</td><td id="68-b">2,160</td></tr>
<tr><td id="68-c">Professional services</td><td id="68-d">1,268</td></tr>
<tr><td id="68-e">Communications and data processing</td><td id="68-f">1,383</td></tr>
<tr><td id="68-g">Amortization of intangibles</td><td id="68-h">82</td></tr>
<tr><td id="68-i">Other non-interest expense:</td><td id="68-j"></td></tr>
<tr><td id="68-k">Bankcard, regulatory and other fee assessments</td><td id="68-l">548</td></tr>
<tr><td id="68-m">Collections</td><td id="68-n">353</td></tr>
<tr><td id="68-o">Other</td><td id="68-p">1,211</td></tr>
<tr><td id="68-q">Total other non-interest expense</td><td id="68-r">2,112</td></tr>
<tr><td id="68-s">Total operating expense</td><td id="68-t">$ 16,307</td></tr>
<tr><td id="68-u">Marketing</td><td id="68-v">4,009</td></tr>
<tr><td id="68-w">Total non-interest expense</td><td id="68-x">$ 20,316</td></tr>
</table>
(b) Credit Card Business Results

<a id='3cb77fa4-2ef7-4d14-ba51-9823991b082e'></a>

<table id="68-y">
<tr><td id="68-z">(Dollars in millions, except as noted)</td><td id="68-A">2023</td></tr>
<tr><td id="68-B">Selected income statement data:</td><td id="68-C"></td></tr>
<tr><td id="68-D">Net interest income</td><td id="68-E">$ 19,729</td></tr>
<tr><td id="68-F">Non-interest income</td><td id="68-G">5,940</td></tr>
<tr><td id="68-H">Total net revenue</td><td id="68-I">25,669</td></tr>
<tr><td id="68-J">Provision (benefit) for credit losses</td><td id="68-K">8,651</td></tr>
<tr><td id="68-L">Non-interest expense</td><td id="68-M">12,490</td></tr>
<tr><td id="68-N">Income from continuing operations before income taxes</td><td id="68-O">4,528</td></tr>
<tr><td id="68-P">Income tax provision</td><td id="68-Q">1,071</td></tr>
<tr><td id="68-R">Income from continuing operations, net of tax</td><td id="68-S">$ 3,457</td></tr>
<tr><td id="68-T" colspan="2">Selected performance metrics:</td></tr>
<tr><td id="68-U">Average loans held for investment</td><td id="68-V">$ 141,572</td></tr>
<tr><td id="68-W">Average yield on loans(2)</td><td id="68-X">18.54%</td></tr>
<tr><td id="68-Y">Total net revenue margin(3)</td><td id="68-Z">18.12</td></tr>
<tr><td id="68-10">Net charge-offs</td><td id="68-11">$ 6,472</td></tr>
<tr><td id="68-12">Net charge-off rate</td><td id="68-13">4.57%</td></tr>
<tr><td id="68-14">Purchase volume</td><td id="68-15">$ 620,290</td></tr>
</table>

<a id='0bc4d11e-0440-4211-bbf7-cf4ceb1bb8fe'></a>

67

<a id='f8b15cd2-16d3-4fda-aa53-7961a5ae9967'></a>

Figure B4: Marketing expenses for credit card banks and other commercial banks

This figure compares the marketing expenses of banks primarily engaged in credit card lending with those of other banks. Quarterly bank-level marketing expenses are from Call Report data from 2010 to 2023 and are expressed as a share of each bank's total assets. We define credit card banks following the Federal Reserve's "Report to the Congress on the Profitability of Credit Card Operations of Depository Institutions", which classifies credit card banks as those where: (1) more than 50% of total assets are loans to individuals, and (2) at least 90% of consumer lending is related to credit cards or similar plans. All numbers are annualized.

<a id='2a55bedc-1c02-45ed-a006-bdf0ebcbf367'></a>

<::Line chart. The y-axis is labeled "Marketing as Share of Assets (%)" and ranges from 0 to 2. The x-axis represents time, with labels at "2010q1", "2013q3", "2017q1", "2020q3", and "2024q1". There are two lines on the chart. The blue line, labeled "Other commercial banks" in the legend, shows a relatively stable and low percentage, generally below 0.1. The red line, labeled "credit card banks" in the legend, shows a more volatile trend, generally ranging between 0.5% and 1.5% from 2010q1 to around 2019. It then drops sharply around 2020q1, recovers, and peaks around 2021q1 at nearly 2%, before declining slightly towards 2024q1.: chart::>

<a id='f3a38533-a45b-40ec-93dd-295469613f98'></a>

68

<a id='88dfdb01-8fb1-4478-9240-37268bc858fe'></a>

Figure B5: Distribution of credit limits

<a id='0fa15ece-a3c4-4cbb-9887-202342da581b'></a>

This figure plots the 25th percentile, median, and 75th percentile of credit limit all across accounts, grouped by FICO scores at account origination in 5-point bins. <::This is a line chart titled "Credit Limit vs. FICO at Origination". The x-axis is labeled "FICO at Origination" and ranges from 600 to 850. The y-axis is labeled "Credit Limit" and ranges from 0 to 25000. There are three lines plotted:
- A blue dashed line representing the 25th percentile (p25).
- A red solid line representing the median.
- A green dashed line representing the 75th percentile (p75).
All three lines show an increasing trend as FICO at Origination increases.: chart::>

<a id='b339fdae-330b-4308-b04a-2278eb54c0a1'></a>

69

<a id='e1ede22b-d5a0-4018-a3f0-92daddaea137'></a>

Figure B6: Return on Assets: Transactors

This figure presents all income and expense components (all on the left y-axis) along with return on assets (ROA) (black line on the right y-axis) for transactors, grouped by FICO scores at account origination in 5-point bins. Transactors are accounts that do not revolve a balance (i.e., are not borrowers). Income components are plotted as positive values, while losses and expenses appear as negative values. By definition, transactors do not incur interest income and credit loss. Non-interest income includes interchange income as computed in Figure 6b plus fee income. Non-interest expense includes rewards income in Figure 6b plus operating expenses, interchange expenses and fraud. All lifetime average rate variables are constructed following the methodology in Section 4: for each origination FICO bin, we compute the cumulative lifetime dollar amount of each component across all accounts in the bin over the entire sample period, then divide it by their cumulative Average Daily Balance (ADB). ROA (net margin) is defined as net interchange income (interchange minus rewards), plus the fee income rate, minus the interest expense, operating expense rate and other non-operating expenses. All rates are annualized.

<a id='3f16290b-d582-4b49-806f-c46482601cf4'></a>

<::Stacked area chart with an overlaid line graph. The x-axis is labeled "FICO at Account Origination" and ranges from 600 to 850. The left y-axis is labeled "Share of Lifetime ADB" and ranges from -0.6 to 0.8. The right y-axis is labeled "ROA" and ranges from -0.02 to 0.18. The stacked areas represent different components:
- Blue area: Interest Income
- Green area: Credit Loss
- Yellow area: Non-Interest Income
- Purple area: Non-Interest Expense
- Red area: Interest Expense
- Dark blue/grey area: Operating Expense
The black line graph represents "ROA (right axis)".
: chart::>

<a id='b14390b6-e2c4-48d9-a428-daa1a97dbe26'></a>

70

<a id='2a4a2ae3-73b2-41e8-8fed-781a7980c9f2'></a>

Figure B7: Return on Assets for credit card banks, other commercial banks and general-purpose credit card loan portfolios

<a id='5ae372ed-f6c4-4c14-87ce-34d5b66d36c4'></a>

This figure presents a time-series comparison of the Return on Assets (ROA) for banks primarily engaged in credit card lending versus other commercial banks, using Call Reports data from 2001 to 2023. Additionally, it includes ROA for general-purpose credit card loan portfolios, based on Y-14M bank portfolio-level data from 2015 to 2023. We define credit card banks following the Federal Reserve's "Report to the Congress on the Profitability of Credit Card Operations of Depository Institutions", which classifies credit card banks as those where: (1) more than 50% of total assets are loans to individuals, and (2) at least 90% of consumer lending is related to credit cards or similar plans. Bank-level ROA from Call Reports is calculated as net income minus provisions for loan losses, divided by total assets. This measure is the same as our credit card lending net margin, except that provisions for credit losses replace net charge-offs. At each point in time, we compute the average ROA for each group by value-weighting individual banks based on their total assets. ROA for general purpose credit card portfolios from Y-14M is defined as interest spread minus provisions for loan losses, plus net interchange income (interchange minus rewards), plus the fee income rate, minus the operating expense rate and other non-operating expenses. All ROA are presented as annualized.

<a id='621a75ae-242d-4b0e-b1c0-cda9acda928a'></a>

<::Line chart showing Return on Assets over time from 2000q1 to 2025q1.

Y-axis: Return on Assets, ranging from -.04 to .12.
X-axis: Time, marked at 2000q1, 2005q1, 2010q1, 2015q1, 2020q1, 2025q1.

Three data series are plotted:
- Blue line: Other Commercial Banks (Call Report), generally stable around .02, dipping slightly below 0 around 2009q1 and 2020q1.
- Red line: Credit Card Banks (Call Report), fluctuating significantly, with peaks around .09 and troughs below 0, especially around 2009q1 and 2020q1.
- Green line: General Purpose Card ROA (Y14M), appearing from around 2015q1, showing a sharp peak above .10 around 2020q1, then declining.

Vertical dashed lines mark two events:
- Around 2008-2009: "Financial Crisis"
- Around 2020: "Covid"
: chart::>

<a id='a16a6a95-7c52-455f-b848-f968f5104565'></a>

71

<a id='092dc570-76fc-45ed-a289-bbcd44158903'></a>

## C Appendix Tables

<a id='34d3843b-f635-4f88-a29b-2f67b4f681d9'></a>

Table C1
Explanatory power of origination FICO score for the charge-off rate
This table reports regressions of charge-off rate, as an outcome variable, with different controls and fixed effects (FE). The observations are at the origination FICO bin × cohort (year-month at origination) × bank level from account-level data. Charge-off rate is the value-weighted average lifetime charge-off rate within each origination FICO-origination month-bank group. "FICO" in the table indicates the average origination FICO level within the bin.
<table id="73-1">
<tr><td id="73-2"></td><td id="73-3" colspan="7">Charge-off Rate</td></tr>
<tr><td id="73-4"></td><td id="73-5">(1)</td><td id="73-6">(2)</td><td id="73-7">(3)</td><td id="73-8">(4)</td><td id="73-9">(5)</td><td id="73-a">(6)</td><td id="73-b">(7)</td></tr>
<tr><td id="73-c">Controls</td><td id="73-d"></td><td id="73-e">FICO</td><td id="73-f">FICO, FICO²</td><td id="73-g"></td><td id="73-h"></td><td id="73-i"></td><td id="73-j"></td></tr>
<tr><td id="73-k">Cohort FE</td><td id="73-l">Y</td><td id="73-m">Y</td><td id="73-n">Y</td><td id="73-o">Y</td><td id="73-p">Y</td><td id="73-q"></td><td id="73-r"></td></tr>
<tr><td id="73-s">Origination FICO FE</td><td id="73-t"></td><td id="73-u"></td><td id="73-v"></td><td id="73-w">Y</td><td id="73-x">Y</td><td id="73-y"></td><td id="73-z"></td></tr>
<tr><td id="73-A">Bank FE</td><td id="73-B"></td><td id="73-C"></td><td id="73-D"></td><td id="73-E"></td><td id="73-F">Y</td><td id="73-G">Y</td><td id="73-H"></td></tr>
<tr><td id="73-I">Origination FICO × Cohort FE</td><td id="73-J"></td><td id="73-K"></td><td id="73-L"></td><td id="73-M"></td><td id="73-N"></td><td id="73-O">Y</td><td id="73-P">Y</td></tr>
<tr><td id="73-Q">Origination FICO × Bank FE</td><td id="73-R"></td><td id="73-S"></td><td id="73-T"></td><td id="73-U"></td><td id="73-V"></td><td id="73-W"></td><td id="73-X">Y</td></tr>
<tr><td id="73-Y">Observations</td><td id="73-Z">32,173</td><td id="73-10">32,173</td><td id="73-11">32,173</td><td id="73-12">32,173</td><td id="73-13">32,173</td><td id="73-14">32,173</td><td id="73-15">32,132</td></tr>
<tr><td id="73-16">R2</td><td id="73-17">0.007</td><td id="73-18">0.085</td><td id="73-19">0.277</td><td id="73-1a">0.311</td><td id="73-1b">0.489</td><td id="73-1c">0.508</td><td id="73-1d">0.728</td></tr>
</table>

<a id='0de7bfc2-3179-4f9e-8b2a-092f5b586e74'></a>

Table C2
Explanatory power of origination FICO score for the APR spread
This table reports regressions of APR spread, as an outcome variable, with different controls
and fixed effects (FE). The observations are at the origination FICO bin × cohort (year-month
at origination) × bank level from account-level data. APR spread refers to average APR mi-
nus Fed funds rate at accounts age of 24 months within each origination FICO-origination month-
bank group. "FICO" in the table indicates the average origination FICO level within the bin.
<table id="73-1e">
<tr><td id="73-1f"></td><td id="73-1g" colspan="7">APR Spread</td></tr>
<tr><td id="73-1h"></td><td id="73-1i">(1)</td><td id="73-1j">(2)</td><td id="73-1k">(3)</td><td id="73-1l">(4)</td><td id="73-1m">(5)</td><td id="73-1n">(6)</td><td id="73-1o">(7)</td></tr>
<tr><td id="73-1p">Controls</td><td id="73-1q"></td><td id="73-1r">FICO</td><td id="73-1s">FICO, FICO²</td><td id="73-1t"></td><td id="73-1u"></td><td id="73-1v"></td><td id="73-1w"></td></tr>
<tr><td id="73-1x">Cohort FE</td><td id="73-1y">Y</td><td id="73-1z">Y</td><td id="73-1A">Y</td><td id="73-1B">Y</td><td id="73-1C">Y</td><td id="73-1D"></td><td id="73-1E"></td></tr>
<tr><td id="73-1F">Origination FICO FE</td><td id="73-1G"></td><td id="73-1H"></td><td id="73-1I"></td><td id="73-1J">Y</td><td id="73-1K">Y</td><td id="73-1L"></td><td id="73-1M"></td></tr>
<tr><td id="73-1N">Bank FE</td><td id="73-1O"></td><td id="73-1P"></td><td id="73-1Q"></td><td id="73-1R"></td><td id="73-1S">Y</td><td id="73-1T">Y</td><td id="73-1U"></td></tr>
<tr><td id="73-1V">Origination FICO × Cohort FE</td><td id="73-1W"></td><td id="73-1X"></td><td id="73-1Y"></td><td id="73-1Z"></td><td id="73-20"></td><td id="73-21">Y</td><td id="73-22">Y</td></tr>
<tr><td id="73-23">Origination FICO × Bank FE</td><td id="73-24"></td><td id="73-25"></td><td id="73-26"></td><td id="73-27"></td><td id="73-28"></td><td id="73-29"></td><td id="73-2a">Y</td></tr>
<tr><td id="73-2b">Observations</td><td id="73-2c">30,366</td><td id="73-2d">30,366</td><td id="73-2e">30,366</td><td id="73-2f">30,366</td><td id="73-2g">30,366</td><td id="73-2h">30,366</td><td id="73-2i">30,332</td></tr>
<tr><td id="73-2j">R2</td><td id="73-2k">0.021</td><td id="73-2l">0.474</td><td id="73-2m">0.505</td><td id="73-2n">0.547</td><td id="73-2o">0.709</td><td id="73-2p">0.722</td><td id="73-2q">0.871</td></tr>
</table>

<a id='6b6eda16-1748-4995-8504-c645a9c62a6a'></a>

72

<a id='4b7c7bac-9fa0-4561-bea6-0d8575270dd8'></a>

Table C3
Distribution of Accounts by Origination FICO score
This table reports the number of accounts and banks, the account share, and the ADB
share across origination FICO bins from account-level data for accounts originated between
January 2015 and December 2017. Account share is the number of accounts in each
FICO bin out of total accounts across all FICO bins. ADB share is the sum of ADB
amounts in each FICO bin divided by the sum of ADB amounts across all FICO bins.
<table id="74-1">
<tr><td id="74-2">Origination FICO</td><td id="74-3">Number of (million)</td><td id="74-4">Accounts</td><td id="74-5">Number of Banks</td><td id="74-6">Account Share</td><td id="74-7">ADB Share</td></tr>
<tr><td id="74-8">550-570</td><td id="74-9">0.2</td><td id="74-a"></td><td id="74-b">20</td><td id="74-c">.007</td><td id="74-d">.004</td></tr>
<tr><td id="74-e">570-590</td><td id="74-f">3.6</td><td id="74-g"></td><td id="74-h">19</td><td id="74-i">.011</td><td id="74-j">.007</td></tr>
<tr><td id="74-k">590-610</td><td id="74-l">57.2</td><td id="74-m"></td><td id="74-n">19</td><td id="74-o">.0178</td><td id="74-p">.012</td></tr>
<tr><td id="74-q">610-630</td><td id="74-r">104.7</td><td id="74-s"></td><td id="74-t">19</td><td id="74-u">.0325</td><td id="74-v">.024</td></tr>
<tr><td id="74-w">630-650</td><td id="74-x">182.9</td><td id="74-y"></td><td id="74-z">20</td><td id="74-A">.0568</td><td id="74-B">.048</td></tr>
<tr><td id="74-C">650-670</td><td id="74-D">255.6</td><td id="74-E"></td><td id="74-F">20</td><td id="74-G">.0791</td><td id="74-H">.080</td></tr>
<tr><td id="74-I">670-690</td><td id="74-J">328.8</td><td id="74-K"></td><td id="74-L">20</td><td id="74-M">.102</td><td id="74-N">.129</td></tr>
<tr><td id="74-O">690-710</td><td id="74-P">331.9</td><td id="74-Q"></td><td id="74-R">20</td><td id="74-S">.103</td><td id="74-T">.133</td></tr>
<tr><td id="74-U">710-730</td><td id="74-V">323.1</td><td id="74-W"></td><td id="74-X">20</td><td id="74-Y">.100</td><td id="74-Z">.125</td></tr>
<tr><td id="74-10">730-750</td><td id="74-11">308.4</td><td id="74-12"></td><td id="74-13">20</td><td id="74-14">.096</td><td id="74-15">.112</td></tr>
<tr><td id="74-16">750-770</td><td id="74-17">283.1</td><td id="74-18"></td><td id="74-19">20</td><td id="74-1a">.088</td><td id="74-1b">.094</td></tr>
<tr><td id="74-1c">770-790</td><td id="74-1d">266.2</td><td id="74-1e"></td><td id="74-1f">20</td><td id="74-1g">.083</td><td id="74-1h">.078</td></tr>
<tr><td id="74-1i">790-810</td><td id="74-1j">282.8</td><td id="74-1k"></td><td id="74-1l">20</td><td id="74-1m">.088</td><td id="74-1n">.066</td></tr>
<tr><td id="74-1o">810-830</td><td id="74-1p">254.8</td><td id="74-1q"></td><td id="74-1r">20</td><td id="74-1s">.079</td><td id="74-1t">.049</td></tr>
<tr><td id="74-1u">830-850</td><td id="74-1v">185.0</td><td id="74-1w"></td><td id="74-1x">20</td><td id="74-1y">.057</td><td id="74-1z">.037</td></tr>
</table>

<a id='e484a6ea-9211-4c05-bb49-0e59241ba8aa'></a>

73