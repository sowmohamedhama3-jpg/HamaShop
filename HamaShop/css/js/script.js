console.log("Bienvenue sur HamaShop !");let panier = JSON.parse(localStorage.getItem("panier")) || [];

// Ajouter un produit
function ajouterPanier(nom, prix) {
    panier.push({ nom, prix });
    localStorage.setItem("panier", JSON.stringify(panier));
    alert(nom + " ajouté au panier !");
}

// Charger le panier
function afficherPanier() {
    let liste = document.getElementById("liste-panier");
    let total = 0;

    panier.forEach((item, index) => {
        total += item.prix;

        let div = document.createElement("div");
        div.innerHTML = `
            <p>${item.nom} - ${item.prix} FCFA</p>
            <button onclick="supprimerItem(${index})">Supprimer</button>
        `;
        liste.appendChild(div);
    });

    document.getElementById("total").innerText = total + " FCFA";
}

// Supprimer un produit
function supprimerItem(index) {
    panier.splice(index, 1);
    localStorage.setItem("panier", JSON.stringify(panier));
    location.reload();}
function validerCommande() {
    let nom = document.getElementById("nom").value;
    let numero = document.getElementById("numero").value;

    let panier = JSON.parse(localStorage.getItem("panier")) || [];

    if (panier.length === 0) {
        document.getElementById("message").innerText = "Panier vide";
        return;
    }

    let total = 0;
    panier.forEach(p => total += p.prix);

    fetch("http://127.0.0.1:5000/commande", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nom: nom,
            numero: numero,
            total: total
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("message").innerText = "Commande envoyée ✔️";
        localStorage.removeItem("panier");
    });
}fetch("http://127.0.0.1:5000/pay", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
        nom: nom,
        numero: numero,
        montant: total
    })
})
.then(res => res.json())
.then(data => {
    document.getElementById("message").innerText =
        "💳 " + data.message;

    localStorage.removeItem("panier");
});