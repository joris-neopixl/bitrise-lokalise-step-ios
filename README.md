# Lokalise

This project can be added to Bitrise as a step to update all translations to an iOS (or Android?) app from Lokalise.

## How to use this Step

### Add the Step to a Workflow
Reference it in your `bitrise.yml` with the `git::PUBLIC-GIT-CLONE-URL@BRANCH` step reference style:

```
- git::https://github.com/joris-neopixl/bitrise-lokalise-step-ios:
   inputs:
   - xxx: yyy
   - zzz: "ttt"
```

### Add secret value

In order to download translations from lokalise, some variable is required.
