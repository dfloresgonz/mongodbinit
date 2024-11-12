### Requerimientos

1. Docker desktop (https://www.docker.com/products/docker-desktop/)
2. Mongodb compass (UI) para visualizar data

### Pasos para instalar

```bash
# levantar el servidor de mongodb
docker-compose up -d
```

### Tutorial video

https://www.loom.com/share/9af2cbace77d48689de198266cc079ec

### Explicación de la solución

https://www.loom.com/share/f39457f5247243088ca5ec7b7530012b


### Queries

```bash
# P1:
db.tweets.find({text: { $regex: "Phillip Butter", $options: "i" } })
```

```bash
# P2:
db.tweets.find({
  $expr: {
    $eq: [
      { $dayOfMonth: { $dateFromString: { dateString: "$date" } } },
      23
    ]
  }
},{
    date: 1,
    text: 1,
    _id: 0
  }).sort({ date: 1 })
.limit(10)
```

```bash
# P3:
db.tweets.aggregate([
  {
    $group: {
      _id: null,
      retweets_count: {
        $sum: {
          $cond: [{ $eq: ["$retweeted", true] }, 1, 0]
        }
      },
      tweets_count: {
        $sum: {
          $cond: [{ $eq: ["$retweeted", false] }, 1, 0]
        }
      }
    }
  }
]);

# otra forma
db.tweets.find({retweeted:false}).count()
db.tweets.find({retweeted:true}).count()
```

```bash
# P4:
db.tweets.find({
  $and: [
    {
      $expr: {
        $eq: [
          { $dayOfMonth: { $dateFromString: { dateString: "$date" } } },
          23
        ]
      }
    },
    {
      text: { $regex: "Phillip Butter", $options: "i" }
    }
  ]
})
```

```bash
# P5: 
db.tweets.aggregate([
  {
    $match: {
      $or: [
        { text: { $regex: "@DanielUrresti1", $options: "i" } },
        { text: { $regex: "@JorgeMunozAP", $options: "i" } }
      ]
    }
  },
  {
    $group: {
      _id: null,
      DanielUrresti1_count: {
        $sum: {
          $cond: [{ $regexMatch: { input: "$text", regex: "@DanielUrresti1", options: "i" } }, 1, 0]
        }
      },
      JorgeMunozAP_count: {
        $sum: {
          $cond: [{ $regexMatch: { input: "$text", regex: "@JorgeMunozAP", options: "i" } }, 1, 0]
        }
      }
    }
  }
]);
```