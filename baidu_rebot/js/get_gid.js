function get_gid() {
var gid = "xxxxxxx-xxxx-3xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,
function(e) {
    var t = 16 * Math.random() | 0,
    n = "x" === e ? t: 3 & t | 8;
    return n.toString(16)
}).toUpperCase();
return gid;
}
