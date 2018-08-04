# Build file using make
make clean
make html

# Move to the project folder
ls
cd docs/html

# Create a new repository
git init
git add .
git commit -am "Automatic Commit"
git push -f git@github.com:sagelga/monopoly-analysis.git master:gh-pages

cd ../../
