mv --force dummy_transformation/ pipa
sed --in-place 's/dummy_transformations/pipa/' tests/test_transformations.py
sed --in-place 's/dummy_transformations/pipa/' .github/workflows/develop.yml