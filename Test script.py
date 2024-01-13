from data_summary import DataSummary 

if __name__ == "__main__":
    try:
        DS_err = DataSummary()  # This should raise an exception
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected DataSummary constructor")

    DS = DataSummary(datafile="Ex1.json", metafile="Happiness Metadata.csv")
    print(DS[3])  # Test __getitem__ by index
    print(DS["Country"])  # Test __getitem__ by key
    try:
        DS['GDP']  # This should raise an exception
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature GDP")

    try:
        DS['data']  # This should raise an exception
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print(DS.mean("Happiness Score"))  # Test mean method
    print(DS.mode("Class"))  # Test mode method
    print(DS.unique("Region"))  # Test unique method

    try:
        DS.min("Country")  # This should raise an exception
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected function min for categorical feature")

    print(DS.max("Happiness Score"))  # Test max method

    test_filename = "test_output.csv"
    DS.to_csv(test_filename)  # Test to_csv method
    print(f"CSV exported to {test_filename}")

    # Clean up: remove the test file
    import os
    os.remove(test_filename)
