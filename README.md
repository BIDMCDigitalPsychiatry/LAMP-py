Steps to regenerate LAMP-py:

1. Copy the current version of the LAMP-server openapi spec into the root directory.
2. Copy `.openapi-generator-ignore.sample` into `./dist`. Name it `.openapi-generator-ignore`.
3. Run `npm install`
4. Run `npm run process_spec <path to open api spec>`
5. Run `npm run generate`