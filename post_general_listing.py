import requests
from requests_oauthlib import OAuth1
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import xml.etree.ElementTree as ET

# Trade Me Sandbox endpoint for selling
url = 'https://api.tmsandbox.co.nz/v1/Selling.xml'

# OAuth1 authentication
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# XML payload as a string
xml_payload = """
<ListingRequest xmlns="http://api.trademe.co.nz/v1">
  <Category>3849</Category>
  <Title>Arty surprise</Title>
  <Description>
    <Paragraph>All true art lovers will buy this.</Paragraph>
  </Description>
  <StartPrice>7</StartPrice>
  <BuyNowPrice>9</BuyNowPrice>
  <Duration>Seven</Duration>
  <Pickup>Allow</Pickup>
  <IsBrandNew>true</IsBrandNew>
  <PhotoIds>
    <PhotoId>12345678</PhotoId>
  </PhotoIds>
  <ShippingOptions>
    <ShippingOption>
      <Type>Free</Type>
    </ShippingOption>
  </ShippingOptions>
  <PaymentMethods>
    <PaymentMethod>CreditCard</PaymentMethod>
    <PaymentMethod>Cash</PaymentMethod>
  </PaymentMethods>
</ListingRequest>
"""

# Set headers to indicate XML content
headers = {
    'Content-Type': 'application/xml'
}

# Send POST request with XML body
response = requests.post(url, data=xml_payload, headers=headers, auth=auth)

# Handle response
if response.status_code == 200:
    print("✅ Listed Successfully:")
    print("Raw XML Response:\n", response.text)

    # Parse XML to extract key info
    root = ET.fromstring(response.text)
    ns = {'ns': 'http://api.trademe.co.nz/v1'}

    listing_id = root.find('.//ns:ListingId', ns)

    print("\nParsed Response:")
    print("Listing ID:", listing_id.text if listing_id is not None else "Not found")

else:
    print(f"❌ Failed: {response.status_code}")
    print("Error Message:\n", response.text)