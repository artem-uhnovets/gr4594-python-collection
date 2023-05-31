```mermaid
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
        D-->A;
```
```mermaid
flowchart LR;
a[input ]-->b[some func];
b-->c{True?};
c--Yes-->d[result];
c--No-->f[another func]


```
```mermaid
    gantt
    title My Product Roadmap
    dateFormat  YYYY-MM-DD
    section Cool Feature
    A task           :a1, 2022-02-25, 30d
    Another task     :after a1, 20d
    section Rad Feature
    Task in sequence :2022-03-04, 12d
    Task, No. 2      :24d
    section 3rd Feature
    Task in sequence :2022-02-25, 50d
```
```mermaid
flowchart TB
    node1[Форма 1]
    node2(Форма 2)
    node3([Форма 3])
    node4[[Форма 4]]
    node5[(Форма 5)]
    node6((Форма 6))
    node7>Форма 7]

```

```mermaid
flowchart TB
    node8{Форма 8}
    node9{{Форма 9}}
    node10[/Форма 10/]
    node11[\Форма 11\]
    node12[/Форма 12\]
    node13[\Форма 13/]

```