document.getElementById("buscar").addEventListener("click", () => {
    const nome = document.getElementById("usuario").value;
    fetch(`https://api.github.com/users/${nome}`) /* sempre que for usar api é esse comando */
    .then((r) => r.json())
    .then((user) => {
        document.getElementById("perfil").innerHTML = `
        <img src="${user.avatar_url}" width="200px"
        <h3>${user.name || "Sem nome"}</h3>
        <p>${user.bio || "Sem bio"}</p>`;
    });

});