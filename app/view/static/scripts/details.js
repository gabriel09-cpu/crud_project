async function abrirModalEdicao(id) {
  const response = await fetch(`http://localhost:8000/api/books/${id}`);
  if (!response.ok) {
    alert("Não foi possível carregar os dados do livro.");
    return;
  }

  const book = await response.json();
  document.getElementById("edit-id").value = id;
  document.getElementById("edit-title").value = book.title || "";
  document.getElementById("edit-author").value = book.author || "";
  document.getElementById("edit-read").checked = book.read || false;
  document.getElementById("edit-page").value = book.page || 0;

  document.getElementById("modalEdicao").style.display = "block";
}

async function salvarEdicao() {
  const id = document.getElementById("edit-id").value;
  const pageValue = document.getElementById("edit-page").value;

  const dadosAtualizados = {
    title: document.getElementById("edit-title").value,
    author: document.getElementById("edit-author").value,
    read: document.getElementById("edit-read").checked,
    page: pageValue ? Number(pageValue) : 0,
  };

  const response = await fetch(`http://localhost:8000/api/books/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dadosAtualizados),
  });

  if (response.ok) {
    alert("Livro atualizado!");
    location.reload();
  } else {
    alert("Erro ao atualizar livro!");
  }
}

function fecharModal() {
  document.getElementById("modalEdicao").style.display = "none";
}