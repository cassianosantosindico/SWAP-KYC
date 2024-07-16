# SWAP-KYC

If you are using the Staging Environment, the KYC analysis response (kyc_status) is determined by the first digit of the value you informed in the document field. The status will be as follows:

- 0-4: Automatically Approved
- 5-6: Automatically Reproved
- 7: In Manual Analysis - followed by Manually Approved
- 8: In Manual Analysis - followed by Manually Reproved
- 9: In Analysis - followed by any final status

# How to run

* `python document_generator.py`
