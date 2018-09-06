    String.prototype.format = function(args) {
        var result = this;
        if (arguments.length > 0) {
            if (arguments.length == 1 && typeof (args) == "object") {
                for (var key in args) {
                    if(args[key]!=undefined){
                        var reg = new RegExp("({" + key + "})", "g");
                        result = result.replace(reg, args[key]);
                    }
                }
            }
            else {
                for (var i = 0; i < arguments.length; i++) {
                    if (arguments[i] != undefined) {
                        var reg= new RegExp("({)" + i + "(})", "g");
                        result = result.replace(reg, arguments[i]);
                    }
                }
            }
        }
        return result;
    }

    function appNode(parentNode,attr) {
        var tag_name,innerText;
        ("tag" in attr)? tag_name=attr["tag"]:tag_name="default_tag";
        ("innerText" in attr)? innerText=attr["innerText"]:innerText="";
        var tag=document.createElement(tag_name);
        tag.innerText=innerText;
        for(var key in attr){
            var filtrer=["tag","innerText","is_before"]
            if (filtrer.includes(key)){continue;}
            tag.setAttribute(key,attr[key]);}
        (attr["is_before"])? parentNode.before(tag):parentNode.append(tag);
    }

