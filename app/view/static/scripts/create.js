async function abrirModalCriacao() {
  const response = await fetch(`http://localhost:8000/books/create`);

  if (!response.ok) {
    alert("Não foi possível conectar!");
    return;
  }

  const new_book = await response.json();
  document.getElementById("add-title").value = new_book.title || "";
  document.getElementById("add-author").value = new_book.author || "";
  document.getElementById("add-page").value = new_book.page || 0;

  document.getElementById("modalCreate").style.display = "block";
}

async function saveBook() {
  const pageValue = document.getElementById("add-page").value;

  const dataCreate = {
    title: document.getElementById("add-title").value,
    author: document.getElementById("add-author").value,
    page: pageValue ? Number(pageValue) : 0,
  };

  const response = await fetch(`http://localhost:8000/books/create`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataCreate),
  });
  if (response.ok) {
    alert("Livro cadastrado!")
  } else {
    alert("Erro ao atualizar livro!")
  }
}

function fecharModal(){
    document.getElementById("modalCreate").style.display = "none";
}