document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("calcForm").addEventListener("submit", function(event) {
        event.preventDefault();
        calculate();
    });
});

function calculate() {
    const vmName = document.getElementById("vm_name").value;
    const backupFrequency = document.getElementById("backup_frequency").value;
    const dataSize = document.getElementById("data_size").value;
    const bandwidth = document.getElementById("bandwidth").value;

    fetch("/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            backup_frequency: backupFrequency,
            data_size: dataSize,
            bandwidth: bandwidth
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("results").innerHTML = `
            <p>RPO: ${data.rpo} minutes</p>
            <p>RTO: ${data.rto} hours</p>
        `;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}