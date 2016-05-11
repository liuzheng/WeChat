var db = openDatabase("WeChat", "0.1", "storage of WeChat", 200000);
if (!db) {
    alert("Failed to connect to database.")
}
else {
    db.transaction(function (tx) {
        tx.executeSql("CREATE TABLE IF NOT EXISTS MemberList (Uin REAL UNIQUE, UserName TEXT,NickName TEXT, HeadImgUrl TEXT,Signature TEXT,PYInitial TEXT,PYQuanPin TEXT,Province TEXT ,City  TEXT,Alias TEXT,DisplayName TEXT,KeyWord TEXT)");
    });
    db.transaction(function (context) {
        context.executeSql('CREATE TABLE IF NOT EXISTS testTable (id UNIQUE, name)');
        context.executeSql('INSERT INTO testTable (id, name) VALUES (0, "Byron")');
        context.executeSql('INSERT INTO testTable (id, name) VALUES (1, "Casper")');
        context.executeSql('INSERT INTO testTable (id, name) VALUES (2, "Frank")');
    });
}
