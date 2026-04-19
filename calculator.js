const form = document.getElementById('calculator');
let p, c, n, m, r, i;
const submitButton = document.getElementById('calculate');
submitButton.addEventListener('click', function (event) {
    // Prevent the default form submission (refresh)
    event.preventDefault();

    const inputs = Array.from(form.querySelectorAll('input[type="text"]'));
    const blankFields = inputs.filter(input => input.value.trim() === "");

    if (blankFields.length > 1) {
        alert(`Error: You have ${blankFields.length} blank fields. Only 1 is allowed.`);
        return;
    }
    if (blankFields.length === 0) {
        alert(`Error: You must leave one field blank.`);
        return;
    };

    p = parseFloat(document.getElementById('P').value);
    c = parseFloat(document.getElementById('C').value / 100);
    n = parseFloat(document.getElementById('N').value);
    m = parseFloat(document.getElementById('M').value);
    r = parseFloat(document.getElementById('r').value / 100);

    inputs.forEach(input => {
        if (input.value.trim() === "") {
            executeLogicFor(input.id);
        }
    });
});

const clearButton = document.getElementById('clear');
clearButton.addEventListener('click', function (event) {
    event.preventDefault();
    document.getElementById('calculator').reset();
});

function executeLogicFor(fieldId) {
    if (fieldId === 'P') solveForP();
    if (fieldId === 'C') solveForC();
    if (fieldId === 'N') solveForN();
    if (fieldId === 'M') solveForM();
    if (fieldId === 'r') solveForr();
}

function solveForP() {
    i = m * c;
    p = i * (1 - (1 + r) ** (-n)) / r + m / ((1 + r) ** n);
    let ea = 1 + r;
    console.log("1+r", ea);
    let eb = ea ** -n;
    console.log("(1+r)^-n", eb);
    let ec = 1 - eb;
    console.log("1 - ((1+r)^-n)", ec);
    let ed = ec / r;
    console.log("(1-((1+r)^-n))/r", ed);
    let ee = c * ed;
    console.log("c*(1-((1+r)^-n))/r", ee);
    let ef = m / ((1 + r) ** n);
    console.log("m/((1+r)**n)", ef);
    document.getElementById("P").value = p;
}

function solveForC() {
    i = (r * p * ((1 + r) ** n) - (m * r)) / ((1 - ((1 + r) ** (-1 * n))) * ((1 + r) ** n));
    c = i / m;
    c = c * 100;
    document.getElementById("C").value = c;
}

function solveForN() {
    i = m * c;
    n = -(Math.log10((p * r - i) / (-i + m * r)) / Math.log10(1 + r));
    document.getElementById("N").value = n;
}

function solveForM() {
    m = 1 / (
        (c / p) * (1 - (1 + r) ** (-n)) / r + 1 / (p * (1 + r) ** n)
    )

    document.getElementById("M").value = m;
}

function solveForr() {
    r = .1;
    i = m * c;
    for (let j = 0; j < 10; j++) {
        r = r - (
            (i * (1 - (1 + r) ** (-n)) / r + m / (1 + r) ** (n) - p) /
            (i * (r * n * (1 + r) ** -(n - 1) + (1 + r) ** (-n) - 1) / r * r + (-m * n * (1 + r) ** (n - 1)) / (1 + r) ** (2 * n))
        )
    }
    r = r * 100;
    document.getElementById("r").value = r;
}
