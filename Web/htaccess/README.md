# HTAccess

by Xaxa

## The Challenge

![Alt text](images\image.png)

## part1: RewriteEngine On
RewriteCond %{HTTP_HOST} !^localhost$
RewriteRule ".*" "-" [F]    

So, if the host != localhost, we get a 403, edit the headers in burp to "Host: localhost"

## part2: RewriteEngine On
RewriteCond %{THE_REQUEST} flag
RewriteRule ".*" "-" [F]

In this case, if we have flag in the request, we get a 403, so just url encode the flag word with burp, and send it again.

