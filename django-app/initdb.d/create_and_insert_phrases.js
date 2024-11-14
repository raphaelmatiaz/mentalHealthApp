db.phrases.drop();

db.createCollection("phrases", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "author", "content", "created_at", "category_id" ],
         properties: {
            author: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            content: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            created_at: {
               bsonType: "string",
               description: "must be a date and is required"
            },
            category_id: {
               bsonType: "int",
               description: "must be an integer and is required"
            }
         }
      }
   }
});

db.phrases.insertMany([
  {
    "author": "Desconhecido",
    "content": "A tristeza é um convite para olhares para dentro e encontrares a tua própria luz.",
    "created_at": "2022-01-01T00:00:00.000Z",
    "category_id": 1
  },
  {
    "author": "Helen Keller",
    "content": "Embora o mundo esteja cheio de sofrimento, ele também está cheio de superação.",
    "created_at": "2022-01-01T00:00:00.000Z",
    "category_id": 1
  },
  {
    "author": "Confúcio",
    "content": "Nossa maior glória não está em nunca cair, mas em nos levantarmos toda vez que caímos.",
    "created_at": "2022-01-01T00:00:00.000Z",
    "category_id": 1
  },
  {
    "author": "Desconhecido",
    "content": "A tristeza não te define, é apenas uma parte do teu caminho.",
    "created_at": "2022-01-01T00:00:00.000Z",
    "category_id": 1
  },
  {
    "author": "Desconhecido",
    "content": "Tudo passa, inclusive as fases tristes. Acredita no amanhã.",
    "created_at": "2022-01-01T00:00:00.000Z",
    "category_id": 1
  },
  {
    "author": "Desconhecido",
    "content": "Lembra-te que o descanso é parte do progresso.",
    "created_at": "2022-02-01T00:00:00.000Z",
    "category_id": 2
  },
  {
    "author": "Albert Einstein",
    "content": "Nem tudo que conta pode ser contado, e nem tudo que pode ser contado conta.",
    "created_at": "2022-02-01T00:00:00.000Z",
    "category_id": 2
  },
  {
    "author": "Desconhecido",
    "content": "Respira. Tudo o que é urgente se resolverá com calma e clareza.",
    "created_at": "2022-02-01T00:00:00.000Z",
    "category_id": 2
  },
  {
    "author": "Winston Churchill",
    "content": "O sucesso não é final, o fracasso não é fatal: o que conta é a coragem de continuar.",
    "created_at": "2022-02-01T00:00:00.000Z",
    "category_id": 2
  },
  {
    "author": "Desconhecido",
    "content": "Trabalha com foco, mas não te esqueças de cuidar de ti.",
    "created_at": "2022-02-01T00:00:00.000Z",
    "category_id": 2
  },
  {
    "author": "Desconhecido",
    "content": "Perdoa-te pelos erros do passado e segue em frente.",
    "created_at": "2022-03-01T00:00:00.000Z",
    "category_id": 3
  },
  {
    "author": "Desconhecido",
    "content": "A culpa é um fardo pesado; liberta-te dela para voares mais alto.",
    "created_at": "2022-03-01T00:00:00.000Z",
    "category_id": 3
  },
  {
    "author": "Oprah Winfrey",
    "content": "Perdoa-te pelo que achas que fez de errado, e lembra-te do teu valor.",
    "created_at": "2022-03-01T00:00:00.000Z",
    "category_id": 3
  },
  {
    "author": "Desconhecido",
    "content": "Cada erro é uma lição. Foca-te no que podes aprender.",
    "created_at": "2022-03-01T00:00:00.000Z",
    "category_id": 3
  },
  {
    "author": "Buda",
    "content": "Você mesmo, tanto quanto qualquer outra pessoa em todo o universo, merece o seu amor e carinho.",
    "created_at": "2022-03-01T00:00:00.000Z",
    "category_id": 3
  },
  {
    "author": "Desconhecido",
    "content": "O teu corpo é o lar da tua alma. Trata-o com amor.",
    "created_at": "2022-04-01T00:00:00.000Z",
    "category_id": 4
  },
  {
    "author": "Desconhecido",
    "content": "A beleza começa no momento em que decides ser tu mesmo.",
    "created_at": "2022-04-01T00:00:00.000Z",
    "category_id": 4
  },
  {
    "author": "Ralph Waldo Emerson",
    "content": "Para ser insubstituível, devemos ser diferentes.",
    "created_at": "2022-04-01T00:00:00.000Z",
    "category_id": 4
  },
  {
    "author": "Desconhecido",
    "content": "Tu és mais do que a tua aparência. A tua essência é o que brilha.",
    "created_at": "2022-04-01T00:00:00.000Z",
    "category_id": 4
  },
  {
    "author": "Desconhecido",
    "content": "  Cada corpo é único e merece respeito e amor.",
    "created_at": "2022-04-01T00:00:00.000Z",
    "category_id": 4
  },
  {
    "author": "Desconhecido",
    "content": "Não tens de ser perfeito para seres aceito.",
    "created_at": "2022-05-01T00:00:00.000Z",
    "category_id": 5
  },
  {
    "author": "Desconhecido",
    "content": "Lembra-te que muitos têm as mesmas inseguranças. És compreendido.",
    "created_at": "2022-05-01T00:00:00.000Z",
    "category_id": 5
  },
  {
    "author": "Maya Angelou",
    "content": "Aprendi que as pessoas esquecerão o que você disse, mas nunca esquecerão como você as fez sentir.",
    "created_at": "2022-05-01T00:00:00.000Z",
    "category_id": 5
  },
  {
    "author": "Desconhecido",
    "content": "A ansiedade é passageira. Respira fundo e vai devagar.",
    "created_at": "2022-05-01T00:00:00.000Z",
    "category_id": 5
  },
  {
    "author": "Desconhecido",
    "content": "A tua presença é valiosa. Lembra-te disso sempre.",
    "created_at": "2022-05-01T00:00:00.000Z",
    "category_id": 5
  },
  {
    "author": "Desconhecido",
    "content": "A tua companhia é mais do que suficiente. Confia no teu próprio valor.",
    "created_at": "2022-06-01T00:00:00.000Z",
    "category_id": 6
  },
  {
    "author": "Helen Keller",
    "content": "Sozinhos, podemos fazer tão pouco; juntos, podemos fazer tanto.",
    "created_at": "2022-06-01T00:00:00.000Z",
    "category_id": 6
  },
  {
    "author": "Desconhecido",
    "content": "A solidão pode ser o início de um grande autoconhecimento.",
    "created_at": "2022-06-01T00:00:00.000Z",
    "category_id": 6
  },
  {
    "author": "Desconhecido",
    "content": "Estar sozinho não significa estar perdido. É uma oportunidade para crescer.",
    "created_at": "2022-06-01T00:00:00.000Z",
    "category_id": 6
  },
  {
    "author": "Desconhecido",
    "content": "A solidão pode ser a chave para uma paz profunda.",
    "created_at": "2022-06-01T00:00:00.000Z",
    "category_id": 6
  },
  {
    "author": "Desconhecido",
    "content": "Confia em ti mesmo. Tens mais força do que pensas.",
    "created_at": "2022-07-01T00:00:00.000Z",
    "category_id": 7
  },
  {
    "author": "Desconhecido",
    "content": "A autoconfiança é o primeiro passo para o sucesso.",
    "created_at": "2022-07-01T00:00:00.000Z",
    "category_id": 7
  },
  {
    "author": "Desconhecido",
    "content": "Lembra-te de quantas vezes superaste os teus próprios limites.",
    "created_at": "2022-07-01T00:00:00.000Z",
    "category_id": 7
  },
  {
    "author": "Desconhecido",
    "content": "A dúvida é apenas uma sombra. O teu valor é real.",
    "created_at": "2022-07-01T00:00:00.000Z",
    "category_id": 7
  },
  {
    "author": "Desconhecido",
    "content": "O primeiro passo para o sucesso é acreditar que mereces.",
    "created_at": "2022-07-01T00:00:00.000Z",
    "category_id": 7
  },
  {
    "author": "Desconhecido",
    "content": "A calma é a chave para venceres a ansiedade.",
    "created_at": "2022-08-01T00:00:00.000Z",
    "category_id": 8
  },
  {
    "author": "Desconhecido",
    "content": "O momento presente é onde a paz vive. Respira e foca-te no agora.",
    "created_at": "2022-08-01T00:00:00.000Z",
    "category_id": 8
  },
  {
    "author": "Desconhecido",
    "content": "Tudo o que vem, também passa. Acalma o teu coração.",
    "created_at": "2022-08-01T00:00:00.000Z",
    "category_id": 8
  },
  {
    "author": "Desconhecido",
    "content": "A ansiedade não define quem és. Respira e recomeça.",
    "created_at": "2022-08-01T00:00:00.000Z",
    "category_id": 8
  },
  {
    "author": "La o Tzu",
    "content": "A natureza não se apressa, mas tudo se realiza.",
    "created_at": "2022-08-01T00:00:00.000Z",
    "category_id": 8
  },
  {
    "author": "Desconhecido",
    "content": "O primeiro passo para o sucesso é acreditar que mereces.",
    "created_at": "2022-09-01T00:00:00.000Z",
    "category_id": 9
  },
  {
    "author": "Desconhecido",
    "content": "A calma é a chave para venceres a ansiedade.",
    "created_at": "2022-09-01T00:00:00.000Z",
    "category_id": 9
  },
  {
    "author": "Desconhecido",
    "content": "Lembra-te de quantas vezes superaste os teus próprios limites.",
    "created_at": "2022-09-01T00:00:00.000Z",
    "category_id": 9
  },
  {
    "author": "Dalai Lama",
    "content": "A paciência é o melhor remédio contra a raiva.",
    "created_at": "2022-09-01T00:00:00.000Z",
    "category_id": 9
  },
  {
    "author": "Desconhecido",
    "content": "Respira fundo. A serenidade é a força real.",
    "created_at": "2022-09-01T00:00:00.000Z",
    "category_id": 9
  },
  {
    "author": "Desconhecido",
    "content": "Escolher o silêncio é um ato de coragem.",
    "created_at": "2022-10-01T00:00:00.000Z",
    "category_id": 10
  },
  {
    "author": "Desconhecido",
    "content": "O controle da raiva começa com o autocontrole.",
    "created_at": "2022-10-01T00:00:00.000Z",
    "category_id": 10
  },
  {
    "author": "Desconhecido",
    "content": "Não esperes pela motivação; começa e a motivação virá.",
    "created_at": "2022-10-01T00:00:00.000Z",
    "category_id": 10
  },
  {
    "author": "Desconhecido",
    "content": "O segredo do progresso é o começo.",
    "created_at": "2022-10-01T00:00:00.000Z",
    "category_id": 10
  },
  {
    "author": "Desconhecido",
    "content": "A cada tarefa concluída, uma nova vitória pessoal.",
    "created_at": "2022-10-01T00:00:00.000Z",
    "category_id": 10
  },
  {
    "author": "Desconhecido",
    "content": "Avançar um pouco a cada dia é melhor que a perfeição adiada.",
    "created_at": "2022-10-01T00:00:00.000Z",
    "category_id": 10
  },
  {
    "author": "Desconhecido",
    "content": "Confia nas tuas conquistas. Elas são fruto do teu trabalho.",
    "created_at": "2022-11-01T00:00:00.000Z",
    "category_id": 11
  },
  {
    "author": "Desconhecido",
    "content": "Lembra-te que mereces estar onde estás.",
    "created_at": "2022-11-01T00:00:00.000Z",
    "category_id": 11
  },
  {
    "author": "Desconhecido",
    "content": "Cada desafio superado é uma prova do teu valor.",
    "created_at": "2022-11-01T00:00:00.000Z",
    "category_id": 11
  },
  {
    "author": "Desconhecido",
    "content": "A tua autenticidade é o teu maior poder.",
    "created_at": "2022-11-01T00:00:00.000Z",
    "category_id": 11
  },
  {
    "author": "Desconhecido",
    "content": "O sucesso é para aqueles que ousam acreditar em si mesmos.",
    "created_at": "2022-11-01T00:00:00.000Z",
    "category_id": 11
  }
]);