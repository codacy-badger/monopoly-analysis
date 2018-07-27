# Make sure the docs is compiled
./buildDocs.sh
cd ../

# Move to the project folder
cd docs/html

# Create a new repository
git init
git add .
git commit -am "Automatic Commit"
git push -f git@github.com:sagelga/monopoly-analysis.git master:gh-pages

# Remove all the git folder, as they are irrelevant now
rm -rf .git
