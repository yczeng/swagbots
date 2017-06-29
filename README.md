# swagBots
Late May 2017, I figured out that theSkimm's referral system had a loophole. When people use your link to subscribe to theSkimm, theSkimm doesn't actually check that the emails are real with a confirmation email. This meant that I could write a bot to artificially put emails into theSkimm to game the system and get swag.

After I maxed out the prize pool for theSkimm's referral system, I wrote bots for similar newsletters Finimize and theHustle.

# How does this work?
swagBots scraped a list of the most common baby names and appended @gmail.com to create subscriber email addresses.

Then it simulated mouse clicks and keyboard strokes to navigate the browsers. Leave it running for a couple hours and see your referral count increase!

# How to Use:
I used [PyUserInput](https://github.com/SavinaRoja/PyUserInput) by SavinRoja, licensed by GPL-3.0, to simulate mouse clicks and keyboard strokes.

```
git clone https://github.com/SavinaRoja/PyUserInput
cd PyUserInput
sudo pip3 install PyUserInput
```
