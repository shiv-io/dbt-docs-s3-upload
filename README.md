## dbt-docs-s3-upload

A proof-of-concept dbt project that deploys dbt docs sites on S3 for each branch. For example, opening a branch `feature-add-x` deploys a docs site on AWS called `dbt-feature-add-x-bucket` with the changes in the branch.

To use, add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to repository secrets (Settings > Secrets > Actions).

For example, see [PR #3](https://github.com/shiv-io/dbt-docs-s3-upload/pull/3).
