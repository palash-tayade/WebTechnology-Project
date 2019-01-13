function checkCookie(){
    var name = "sessionid" + "=";
    var decodedCookie = decodeURIComponent(document.cookie);

    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            var session_val=c.substring(name.length, c.length);
            if(parseInt(session_val.length) != 0){
            var myNode = document.getElementById("formHead");
            while (myNode.firstChild) {
            myNode.removeChild(myNode.firstChild);
            }

            var my_form=document.createElement('FORM');
            my_form.id='logoutform ';
            my_form.method='POST';
            my_form.action='/logout';


            var my_div=document.createElement('DIV');
            my_div.setAttribute("class","loginDiv");

            var my_tb=document.createElement('INPUT');
            my_tb.type='Submit';
            my_tb.name='logout';
            my_tb.value='Log Out';
            //my_tb.class='logoutButton';
            my_tb.setAttribute("class","loginButton")
            my_div.appendChild(my_tb);

            my_form.appendChild(my_div);

            myNode.appendChild(my_form);

            //Dynamically creating Post Job Form

            var body= document.getElementById("postform");

            var form=document.createElement('FORM');
            form.id='postform ';
            form.method='POST';
            form.action='/postJob';

            body.appendChild(form);

            var first_container=document.createElement('DIV');
            first_container.setAttribute("class","imgFirstContainer");

            body.appendChild(first_container);




            var second_container=document.createElement('DIV');
            second_container.setAttribute("class","imgSecondContainer");

            first_container.appendChild(second_container);

            var form=document.createElement('FORM');
            form.id='postform';
            form.method='POST';
            form.action='/post';

            second_container.appendChild(form);

            var h4 = document.createElement("h4");
            h4.textContent = "Post a Job !";

            second_container.appendChild(h4)




            var x = document.createElement("TABLE");
            x.setAttribute("id", "myTable");
            form.appendChild(x);



            var y = document.createElement("TR");
            document.getElementById("myTable").appendChild(y);

            var z = document.createElement("TD");

            var col_label=document.createElement("LABEL");
            var text = document.createTextNode("Contact: ");
            col_label.appendChild(text);
            //col_label.setAttribute("for", "contact");
            col_label.appendChild(text);

            z.appendChild(col_label);
            y.appendChild(z);

            z = document.createElement("TD")
            col_type=document.createElement("INPUT");
            col_type.setAttribute("type","text");
            col_type.setAttribute("class","loginText");
            col_type.setAttribute("name","contact");
            z.appendChild(col_type);
            y.appendChild(z);

            //for position
            var y = document.createElement("TR");
            document.getElementById("myTable").appendChild(y);

            z = document.createElement("TD");
            col_label=document.createElement("LABEL");
            text = document.createTextNode("Position: ");
            col_label.appendChild(text);
            z.appendChild(col_label);
            y.appendChild(z);

            z = document.createElement("TD")
            col_type=document.createElement("INPUT");
            col_type.setAttribute("type","text");
            col_type.setAttribute("class","loginText");
            col_type.setAttribute("name","position");
            z.appendChild(col_type);
            y.appendChild(z);


            //for location
            var y = document.createElement("TR");
            document.getElementById("myTable").appendChild(y);

            z = document.createElement("TD");
            col_label=document.createElement("LABEL");
            text = document.createTextNode("Location: ");
            col_label.appendChild(text);
            z.appendChild(col_label);
            y.appendChild(z);

            z = document.createElement("TD")
            col_type=document.createElement("INPUT");
            col_type.setAttribute("type","text");
            col_type.setAttribute("class","loginText");
            col_type.setAttribute("name","location");
            z.appendChild(col_type);
            y.appendChild(z);


            //for company
            var y = document.createElement("TR");
            document.getElementById("myTable").appendChild(y);

            z = document.createElement("TD");
            col_label=document.createElement("LABEL");
            text = document.createTextNode("Company: ");
            col_label.appendChild(text);
            z.appendChild(col_label);
            y.appendChild(z);

            z = document.createElement("TD")
            col_type=document.createElement("INPUT");
            col_type.setAttribute("type","text");
            col_type.setAttribute("class","loginText");
            col_type.setAttribute("name","company");
            z.appendChild(col_type);
            y.appendChild(z);



             //for description
            var y = document.createElement("TR");
            document.getElementById("myTable").appendChild(y);

            z = document.createElement("TD");
            col_label=document.createElement("LABEL");
            text = document.createTextNode("Description: ");
            col_label.appendChild(text);
            z.appendChild(col_label);
            y.appendChild(z);

            z = document.createElement("TD")
            col_type=document.createElement("INPUT");
            col_type.setAttribute("type","text");
            col_type.setAttribute("class","loginText");
            col_type.setAttribute("name","description");
            z.appendChild(col_type);
            y.appendChild(z);

            //Submit button
            //var y = document.createElement("TR");
            //document.getElementById("myTable").appendChild(y);


            //z = document.createElement("TD")
            my_tb=document.createElement('INPUT');
            my_tb.type='Submit';
            my_tb.name='postjob';
            my_tb.value='Post Job';

            //my_tb.setAttribute("class","loginButton")
            //z.appendChild(my_tb);
            //y.appendChild(z);
            form.appendChild(my_tb)



            }
        }
    }

    }

    window.onload=checkCookie