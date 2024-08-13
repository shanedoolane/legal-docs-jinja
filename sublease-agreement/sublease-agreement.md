# STANDARD RESIDENTIAL SUB-LEASE AGREEMENT
THIS LEASE AGREEMENT hereinafter known as the "Lease" is entered into this {{ day }} 
day of {{ month }}, {{ year }}, by and between {{ landlord_name }} with mailing
address at {{ address }} hereinafter known
as the "Landlord" and {{ tenant_1 }} hereinafter known as the "Tenant(s)."

WHEREAS, the Landlord desires to lease the Property defined herein under the
terms and conditions as set forth herein; and
WHEREAS, the Tenant(s) desires to lease the Property defined herein from the
Landlord under the terms and conditions set forth herein.

NOW, THEREFORE, for and in consideration of the covenants and obligations
contained herein and other good and valuable consideration, the receipt and
sufficiency of which is hereby acknowledged, the Parties hereby agree as follows:

## PROPERTY
{{ address }} (hereinafter referred to as the "Property").

## LEASE TERM
This Lease shall commence at {{lease_start_datetime_utc}} UTC, and 
end on {{lease_end_datetime_utc}} UTC (hereinafter referred to
as the "Term"), unless otherwise terminated in accordance with the provisions of the
Lease. Upon the end of the Term, Tenant(s) shall vacate the Property and deliver the
same to the Landlord unless:

- The Lease is formally extended by the Landlord and the Tenant(s) in writing
signed by both Parties

OR

- The Landlord willingly accepts Rent from the Tenant(s) for a period beyond the
original Term. Where the Landlord accepts Rent for a period beyond the
original Term, without a formal extension agreed to in writing by both Parties,
a month-to-month tenancy will be created.

## Rent
The Tenant(s) shall pay to the Landlord the sum of ${{ rent }} USD per month
(hereinafter referred to as "Rent") for the duration of the Term of the Lease. The Rent
shall be payable on or before every {{ rent_day }} day of the month (hereinafter referred to as
the "Due Date"), notwithstanding that the said date falls on a weekend or holiday.

### 1. Late Rent
If Rent is not paid within {{ max_late_days }} day(s) of the Due Date, the Rent shall
be considered past due and a late fee of ${{ late_fee }} USD and {{ late_percent }} % of the
Rent past due shall be applied for every {{ late_rent_period }} day(s) Rent is late.
### 2. Returned Checks
In the event that a check intended as payment for Rent is
dishonoured for whatever reason, the same shall be considered as Late Rent
with the late fee being payable on the same.
### 3. Application of Payments
Whenever there are different sums owed by the
Tenant(s) to the Landlord, any payment shall be applied first to those 2 obligations 
other than Rent including but not limited to
association/community dues, Late Fee, repairs chargeable to the Tenant(s),
and other charges notwithstanding any notations or specifications made by
the Tenant(s) on the application of any payment paid to the Landlord.
### 4. Rent Increases
The Rent payable shall not be increased or otherwise
modified during the Term of this Lease. Any increase in Rent shall only take
effect after the expiration of the Term provided in this Lease. Any increase in
Rent to take effect upon renewal or extension of the Term of this Lease must
be preceded by a {{ rent_increase_notification_period_days }} day notice of the same from the Landlord to the
Tenant(s).
### 5. Method of Payment
The Landlord accepts Rent payments made using {{ payment_methods_list }}.
### 6. Formula for Calculation of Pro-rated Rent
The Landlord uses the following formula for determining the prorated rental amount applied to any month: 
{{ pro_rate_formula }} where "Days Stayed" is any day on which the Tenant exists in the Property and including each
day of the Term.

## Security Deposit
The Tenant(s) shall handover to the Landlord the amount of
${{ security_deposit_full }} USD as Security Deposit upon the execution of this Lease (the "Security
Deposit"). The receipt of such Security Deposit is hereby acknowledged by the
Landlord who undertakes to hold the same in compliance with applicable laws,
rules, and regulations.

### 1. Deductions
Upon the termination of the Lease, the Landlord may deduct the
following from the Security Deposit:
{% if deduct_unpaid_rent %}
- Unpaid rent
{% endif %}
{% if deduct_unpaid_late_fees %}
- Late fees
{% endif %}
{% if deduct_unpaid_utilities %}
- Unpaid utilities
{% endif %}
{% if deduct_repairs %}
- Cost of repairs beyond ordinary wear and tear
{% endif %}
{% if deduct_cleaning_fee %}
- A minimum cleaning fee of ${{ cleaning_fee_minimum }} USD if the apartment is not as clean as it was 
when the Tenant moved in after the Term. 
{% endif %}
{% if deduct_early_termination_fee %}
- Early termination fee 
{% endif %}
{% if deduct_brokerage_fee %}
- Brokerage fees
{% endif %} 
{% if deduct_others %}
- Others: {{ others }}
{% endif %}

### 2. Return 
The Security Deposit or the balance thereof shall be returned by the
Landlord to the Tenant(s) within {{ security_deposit_return_days }} days after the termination of the Lease
or in accordance with the applicable law on Security Deposit, whichever is
sooner. In the event that the Landlord shall make any allowable deduction,
the Landlord shall provide the Tenant(s) with an itemized list of all deductions
made specifying the amounts and the respective expenses to which the
Security Deposit or parts of it was applied.

### 3. Tenant's Forwarding Address
Upon vacating the Property any and all
notices, communication and any other delivery may be made to the Tenant's
forwarding address at: {{ tenant_forwarding_address }}

### 4. Termination of the Lease Before Term Origin
In the event the Tenant desires to terminate the lease before the origin of the Term. 
The deduction from the security deposit
for early termination will be ${{ pre_origin_termination_fee }} USD 
in addition to other applicable deductions outlined in the lease or permitted by law.

## USE OF PROPERTY
The Property as defined herein shall be for the sole and
exclusive use and occupation by the Tenant(s) and same's exclusive family namely: {{ tenants_family_members }}

Any Guest(s) of the Tenant(s) shall not be allowed to stay beyond {{ max_days_guest }} days without
the consent of the Landlord. The Property shall be used solely and exclusively as a
residence. The Property or any part of it shall not be used for any business, profession, vocation, 
or trade of any kind. The Tenant(s) undertake(s) to abide by any
and all applicable laws, statutes, and rules covering the Property.

## CONDITION
The Tenant(s) stipulates that The Property has been examined and that
the Property is in good repair and is tenantable.

## ASSIGNMENT 
Under this Lease:
{% if subletting_allowed %}
### Subletting Allowed.
Tenant(s) shall have the right to sublet and grant a license to
other individuals to use the Property or any part thereof with the prior
written consent of the Landlord. In the event the Tenant(s) shall sublet the Property,
notice shall be given to the Landlord within {{ sublease_notification_days }} days of the Subtenant(s) name and
address. In the event the Subtenant(s) violates any portion of this Lease, all liability
shall be held against the Tenant(s).
{% else %}
### Subletting Not Allowed.
The Tenant(s) acknowledges that this Lease is not
transferrable and that the Tenant(s) may not assign the Lease, any part of the Lease
or any of the rights or obligations herein. The Tenant(s) shall not sublet, sublease, or
otherwise grant any other party any license or right in relation to the Property or this
Lease. Any license, assignment sublease or agreement in violation of this clause shall
be null and void with no legal force whatsoever.
{% endif %}

## RIGHT OF ENTRY
The Landlord shall have the right to enter the Property during
normal working hours by providing at least {{ right_of_entry_notification_hours }} hour(s) notice 
in order for inspection,
make necessary repairs, alterations or improvements, to supply services as agreed or
for any reasonable purpose. The Landlord may exhibit the Property to prospective
purchasers, mortgagees, or lessees upon reasonable notice.

## ALTERATIONS AND IMPROVEMENTS
No alterations to or improvements on the
Property shall be made by the Tenant(s) without prior express consent of the
Landlord to the same in writing.

### 1. Unauthorized Alterations or Improvements
In the event that the Tenant(s)
shall undertake alterations or improvements relating to the Property in
violation of this section the same shall be considered a material breach of this
Lease putting the Tenant(s) in default. The Landlord may, upon the Landlord's
discretion, require the Tenant(s) to undo the alterations or improvements and
restore the Property to its condition prior to any unauthorized alteration or
improvement at the sole expense of the Tenant(s).

### 2. Ownership of Alterations and Improvements
In all cases of alterations,
improvements, changes, accessories, and the like that cannot be removed
from the Property without destroying or otherwise deteriorating the Property
or any surface thereof shall, upon creation, become the Landlord's property
without the need for any further transfer, delivery, or assignment thereof.

## NON-DELIVERY OF POSSESSION
The Landlord shall deliver to the Tenant(s)
possession of the Property on or before the commencement of the Term of this
Lease. Delay in the delivery of possession of the Property for any cause other than
the fault or negligence of the Landlord shall cause the abatement of the Rent until
the date until such time the possession is delivered. In any event, the possession of
the Property must be delivered no later than {{ non_deliver_possession_duration_days }} days after the commencement of
the Term of this Lease and the Tenant(s) agree(s) to accept the same until such date
despite the delay. Failure of the Landlord to deliver possession of the Property within
this period, shall automatically terminate the Lease. Upon such Termination, the
Landlord shall return to the Tenant(s) the Security Deposit, any advance Rent and
other sums not otherwise consumed on account of the Tenant(s) never having
occupied the Property such as, but not limited to cleaning fees if already collected.
Thereafter the Parties shall have no further obligation to each other.

## HAZARDOUS MATERIALS
Tenant(s) shall not keep on the Property any item of a
dangerous, flammable, or explosive nature that might unreasonably increase the
danger of fire or explosion on the Property or that might be considered hazardous or
extra hazardous by any responsible insurance company.

## UTILITIES
The Landlord shall provide the following utilities and services to the
Tenant(s) without cost: {{ utilities_provided_by_landlord }}.

The Tenant shall equally split the cost of following utilities and services with the Landlord
Tenant(s): {{ utilities_split_with_tenant }}.

Any other utilities or services not mentioned will be the responsibility of the Tenant(s).

## MAINTENANCE, REPAIR, AND RULES
The maintenance of the Property, minor
repairs, and servicing shall be the responsibility and sole expense of the Tenant(s),
including but not limited to HVAC/air-conditioning units, plumbing fixtures (e.g.,
showers, bathtubs, toilets, or sinks). For the entirety of the term of this Lease, the
Tenant(s) shall keep the property clean and in good repair. The Tenant(s) shall:

1. Comply with any and all rules or regulations covering the Property
including but not limited to local ordinances, health or safety codes,
those set forth in the Master Lease, and Condominium or Homeowner's
associations, where applicable.
2. Dispose of any and all waste properly.
3. Not obstruct any structure intended for ingress, egress, passage or
otherwise providing some type of access to, from or through the
property.
4. Keep all windows, balconies, railings and other fixtures or structures
visible from outside of the property free from laundry at all times.
5. Obtain consent of the Landlord prior to replacing or installing new
deadbolts, locks, hooks, doorknobs, and the like.
6. Refrain from all activities that will cause unreasonable loud noises or
otherwise unduly disturb neighbors and/or other residents.

## PETS
Under this Lease:
{% if pets_allowed %}
### Pets Allowed.
<!-- todo: this section is not created -->
The Tenant(s) shall be allowed to have ____ pet(s) on the Property
consisting of ☐ Dogs ☐ Cats ☐ Fish ☐ Other _______________________ not weighing
more than ____ ☐ pounds. The Landlord shall administer a fee of $____________ per
pet on the Property. Landlord shall be held harmless in the event any of the Tenant's
pets cause harm, injury, death, or sickness to another individual or animal. Tenant(s)
is responsible and liable for any damage or required cleaning to the Property caused
by any authorized or unauthorized animal and for all costs Landlord may incur in
removing or causing any animal to be removed.
{% else %}
### Pets Not Allowed.
There shall be no animals permitted on the Property or in any
common areas UNLESS said pet is legally allowed under the law in regard to
assistance with a disability. Pets shall include, but not be limited to, any mammal,
reptile, bird, fish, rodents, or insects on the Property.
{% endif %}

## QUIET ENJOYMENT
The Landlord warrants that the Tenant(s) shall have quiet and
peaceful enjoyment of the Property and hold the same free from molestation or
interference from the Landlord or any other person or entity whose claim to the
Property comes from the Landlord, subject to the terms and conditions of this Lease
and compliance by the Tenant(s) with the same.

## Indemnification
The Landlord shall not be liable for any injury to the Tenant(s) or
any other persons or property entering the Property occurring within the Property
during the Term of the Lease. Neither shall the Landlord be liable for any damage to
the structure within which the Property is located or any part thereof. The Tenant(s)
hereby agrees to hold the Landlord harmless from and indemnify the Landlord for
any and all claims or damage not arising solely from the Landlord's acts, omission,
fault, or negligence.

## DEFAULT
In the event that the Landlord breaches any of the terms and conditions
of this Lease or any applicable laws, rules, or codes, the Tenant(s) may avail of any of
the remedies available under the law. In the event that the Tenant(s) breaches or
fails to comply with any of the terms and conditions of this Lease or any applicable
laws, rules, or codes the Landlord shall afford the Tenant(s) days to remedy or
rectify the same. This period shall commence on the day the Tenant(s) receives
Notice of such breach or non-compliance with the request to rectify the same. If the
Tenant(s) fail(s) to comply or rectify the breach or if the breach cannot reasonably be
rectified or remedied, the Tenant(s) shall be in default. Upon the Tenant's default, the
Landlord may terminate the Lease by sending the notice of default and consequent
termination of the lease to the Tenant(s) and thereafter recover possession of the
Property.

## ABANDONMENT
In the event that the Tenant(s) abandon(s) the Property the
Landlord may declare the Lease terminated, recover possession of the Property,
enter the premises, remove the Tenant's belongings and lease the same to another
without incurring any liability to the Tenant(s) for doing the same. In the event of the
abandonment of the Property, the Landlord may recover from the Tenant(s) unpaid
Rent until the Property is leased to another person or otherwise occupied by the
Landlord or another under the Landlord's right.

## ATTORNEYS' FEES
In the event that Landlord should require the services of an
attorney, file a suit or resort to other procedures in order to compel the Tenant's
compliance with the Tenant's obligations, the terms of this Lease or other applicable
laws, rules, or codes, the Tenant(s) agree(s) to reimburse all expenses incurred by the
Landlord in doing the same.

## COMPLIANCE WITH LAW
The Tenant(s) undertakes to comply with any and all
Federal or state laws, municipal or county ordinances, rules, regulations, codes, and all other issuances from 
authorized government authorities respecting the Property
and the Tenant's occupation and use thereof.

## SEVERABILITY
Should any provision of this Lease be found, for whatever reason,
invalid or unenforceable, such nullity or unenforceability shall be limited to those
provisions. All other provisions herein not affected by such nullity or dependent on
such invalid or unenforceable provisions shall remain valid and binding and shall be
enforceable to the full extent allowed by law.

## BINDING EFFECT
The terms, obligations, conditions, and covenants of this Lease
shall be binding on Tenant(s), the Landlord, their heirs, legal representatives, and
successors in interest and shall inure to the benefit of the same.

## MODIFICATION
The Parties hereby agree that this document contains the entire
agreement between the Parties and this Lease shall not be modified, changed,
altered, or amended in any way except through a written amendment signed by all
of the Parties hereto.

## NOTICE
All notices in relation to this Lease shall be delivered to the following
addresses:

To the Tenant(s) at the address: 
{{ address }} 

and 

To the Landlord at the address:
{{ address }}

## PARKING
The Landlord {% if parking_provided %}
shall provide {{ parking_spots }} parking spots to the Tenant(s) for a fee of ${{ parking_fee }} USD 
to be paid on a monthly basis in addition to the Rent. 

The parking space(s) are described as: {{ description_of_parking_spot }}
{% else %}
shall not provide parking.
{% endif %}

## EARLY TERMINATION
<!-- todo: replace early termination fee with math (i.e. multiply by 2 or whatever) -->
The Tenant(s) {% if ability_to_terminate_lease_early %}
Shall have the right to terminate this Lease at any time by providing at least {{ early_termination_notice_days }}
days' written notice to the Landlord along with an early termination fee of ${{ early_termination_fee }} USD.
During the notice period for termination, the Tenant(s) will remain responsible for
the payment of Rent.
{% else %}
Shall not have the right to terminate this Lease before the end of the Term.
{% endif %}

## SMOKING POLICY
Smoking on the Property is {% if smoking_allowed %} permitted in the following areas: {{ smoking_allowed_areas }}.
{% else %}
Prohibited on the Property and its premises.
{% endif %}

## DISPUTES
If a dispute arises during or after the term of this Lease between the
Landlord and Tenant(s), they shall agree to hold negotiations amongst themselves,
in "good faith", before any litigation.

## RETALIATION
The Landlord is prohibited from making any type of retaliatory acts
against the Tenant(s) including but not limited to restricting access to the Property,
decreasing, or cancelling services or utilities, failure to repair appliances or fixtures, or
any other type of activity that could be considered unjustified.

## EQUAL HOUSING
If the Tenant(s) possesses any impairment, mental or physical, the
Landlord agrees to provide reasonable modifications to the Property in order to
accommodate such impairments except in the case of modifications that would be
too difficult or too expensive for the Landlord to provide. The Tenant(s) is/are
encouraged to disclose to the Landlord any impairment(s) that may be aided by
reasonable modifications to allow the Parties to identify the most beneficial
modifications to the Property.

## PROPERTY DEEMED UNINHABITABLE
If the Property is deemed uninhabitable
due to damage beyond reasonable repair the Tenant(s) will be able to terminate this
Lease by written notice to the Landlord. If said damage was due to the negligence of
the Tenant(s), the Tenant(s) shall be liable to the Landlord for all repairs and for the
loss of income due to restoring the property back to a livable condition in addition to
any other losses that can be proved by the Landlord.

## LEAD-BASED PAINT DISCLOSURE
If the Property or any part of it was constructed
prior to 1978, the Landlord shall provide a disclosure of information on lead-based
paint and/or lead-based paint hazards, the receipt of the same in the form entitled
“LEAD-BASED PAINT DISCLOSURE” hereby acknowledged by the Tenant(s).

## ENTIRE AGREEMENT
This Lease and, if any, attached documents are the complete
agreement between the Landlord and Tenant(s) concerning the Property. There are
no oral agreements, understandings, promises, or representations between the
Landlord and Tenant(s) affecting this Lease. All prior negotiations and
understandings, if any, between the Parties hereto with respect to the Property shall
be of no force or effect and shall not be used to interpret this Lease. No modification
or alteration to the terms or conditions of this Lease shall be binding unless expressly
agreed to by the Landlord and the Tenant(s) in a written instrument signed by both
Parties.

## IN WITNESS WHEREOF
The Landlord and Tenant(s) have executed this Lease in
multiple originals as of the undersigned date(s).

#### Landlord's Signature: 
{{ landlord_signature }} 
Date: {{ day }} day of {{ month }}, {{ year }}
#### Print Name:
{{ landlord_name }}

#### Tenant's Signature: 
{{ tenant_signature }}
Date: {{ tenant_signature }}
#### Print Name:
{{ tenant_1 }}