var xhr = new XMLHttpRequest();
xhr.open('GET', '/data', true);
xhr.onload = function() {
    if (this.status === 200) {
        var data = JSON.parse(this.responseText);
        var tbody = document.getElementById('table-body');
        for (var i = 0; i < data.length; i++) {
            var tr = document.createElement('tr');
            var tdName = document.createElement('td');
            tdName.innerText = data[i].name;
            tr.appendChild(tdName);
            var tdAge = document.createElement('td');
            tdAge.innerText = data[i].age;
            tr.appendChild(tdAge);
            var tdEmail = document.createElement('td');
            tdEmail.innerText = data[i].email;
            tr.appendChild(tdEmail);
            tbody.appendChild(tr);
        }
    }
};
xhr.send();