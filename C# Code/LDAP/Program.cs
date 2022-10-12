DirectoryEntry directoryEntry = new DirectoryEntry("LDAP://example.com");
DirectorySearcher searcher = new DirectorySearcher(directoryEntry) {
    PageSize = int.MaxValue,
    Filter = "(&(objectCategory=person)(objectClass=user)(sAMAccountName=AnAccountName))"
};

searcher.PropertiesToLoad.Add("sn");

var result = searcher.FindOne();

if (result == null) {
    return; // Or whatever you need to do in this case
}
string surname;

if (result.Properties.Contains("sn")) {
    surname = result.Properties["sn"][0].ToString();
}