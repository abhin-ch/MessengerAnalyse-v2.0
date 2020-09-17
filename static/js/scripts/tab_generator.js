
for(var i=0; i<a_name.length ; i++){
    var name = a_name[i];
    var id = name.split(" ").join(""); 
    var res1 = "#";
    var href =  res1.concat(id);
    var ls = document.createElement('li');
    ls.classList.add("nav-item");
    var a = document.createElement('a');
    if (i==0) {
        var bool = "true";
        a.setAttribute("class","nav-link active");
      }
    else{
        var bool = "false";
        a.setAttribute("class","nav-link");
    }
    a.setAttribute("data-toggle","tab");
    a.setAttribute("href", href);
    a.setAttribute("role", "tab");
    a.setAttribute("aria-expanded", bool);
    a.textContent = name;
    ls.appendChild(a);
    var ul = document.getElementById("tabs");
    ul.appendChild(ls);
}
