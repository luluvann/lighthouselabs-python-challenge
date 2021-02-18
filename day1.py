# Day1 - Modify a lease agreement with your signature without changing the original lease variable.

lease = '''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: '''
            
signature = 'MySignature'

# Solution

new_lease_signed = f'{lease} {signature}

print(new_lease_signed)

