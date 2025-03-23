firebase.json should have multiple sites configured under the hosting key:

{
  "hosting": [
    {
      "site": "quantumsafe-multisig",
      "public": "public",
      "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
      "headers": [
        {
          "source": "**/*.css",
          "headers": [{ "key": "Content-Type", "value": "text/css" }]
        }
      ]
    },
    {
      "site": "quantumsafe-multisig-pin4321",
      "public": "public-pin",
      "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
      "headers": [
        {
          "source": "**/*.css",
          "headers": [{ "key": "Content-Type", "value": "text/css" }]
        }
      ]
    }
  ]
}


2. Deploy to a Specific Site
use --only hosting with the actual site name (not target):
Deploy only to quantumsafe-multisig.web.app:
$ firebase deploy --only hosting:quantumsafe-multisig

Deploy only to quantumsafe-multisig-pin4321.web.app:
$ firebase deploy --only hosting:quantumsafe-multisig-pin4321

Deploy both sites together:
$ firebase deploy --only hosting
