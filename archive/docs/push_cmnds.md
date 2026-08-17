# Git Push Commands

When there are remote changes (e.g., from automated GitHub Actions) and you have local changes, use this safe sequence:

```bash
git stash          # 1. Temporarily save your uncommitted changes
git pull           # 2. Fetch and merge the latest remote changes
git stash pop      # 3. Restore your uncommitted changes
git push           # 4. Push your commits to GitHub
```

# 1. Stage all the current changes
git add .
# 2. Commit the changes
git commit -m "Use absolute raw URLs for table images so they load on profile page"
# 3. Pull the remote changes from GitHub and place our local commit on top (this fixes the 'rejected' error)
git pull --rebase
# 4. Push everything back up to GitHub
git push



git add -f "Main Banner.gif" "Thank you Banner.gif"
git commit -m "Add banners"
git push