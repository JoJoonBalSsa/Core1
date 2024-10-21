# 결과 보고서

**생성일:** 2024-10-19 15:46:10

**생성 도구:** Taint Bomb

## 목차
- [개요](#개요)
- [흐름 1: line](#흐름-1-line) - 상
- [흐름 2: line_1](#흐름-2-line_1) - 상
- [흐름 3: balance](#흐름-13-balance) - 상
- [흐름 4: balance_1](#흐름-14-balance_1) - 상
- [흐름 5: line](#흐름-15-line) - 중
- [흐름 6: leftMenus](#흐름-16-line_1) - 중


## 개요
이 보고서는 코드베이스에 대한 분석 결과를 제공하며, 잠재적인 보안 위험과 취약점을 식별합니다.
각 섹션에는 오염된 데이터의 흐름을 시각화한 콜 그래프와 상세 정보가 포함되어 있습니다.

## 콜 그래프
아래는 애플리케이션에서 오염된 데이터의 흐름을 나타내는 콜 그래프입니다. 각 그래프 뒤에는 관련된 오염된 변수에 대한 상세 분석이 이어집니다.

## 흐름 1: `line` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="465.0" y="10" width="270" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SocketClient</text><g id="EventControl_SocketClient_getInputStream"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getInputStream</text><text x="708.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_SocketClient_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `line`

**데이터 흐름:**
```
EventControl.SocketClient.getInputStream -> EventControl.SocketClient.getInputStream -> EventControl.SocketClient.println
```

## 흐름 2: `line_1` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="465.0" y="10" width="270" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SocketClient</text><g id="EventControl_SocketClient_getInputStream"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getInputStream</text><text x="708.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_SocketClient_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `line_1`

**데이터 흐름:**
```
EventControl.SocketClient.getInputStream -> EventControl.SocketClient.getInputStream -> EventControl.SocketClient.println
```

## 흐름 3: `line_2` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="465.0" y="10" width="270" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SocketClient</text><g id="EventControl_SocketClient_getInputStream"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getInputStream</text><text x="708.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_SocketClient_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `line_2`

**데이터 흐름:**
```
EventControl.SocketClient.getInputStream -> EventControl.SocketClient.getInputStream -> EventControl.SocketClient.println
```

## 흐름 4: `id` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `id`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 5: `id_1` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `id_1`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 6: `name` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 7: `name_1` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name_1`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 8: `balance` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `balance`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 9: `balance_1` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `balance_1`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 10: `id_2` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `id_2`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 11: `name_2` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name_2`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 12: `balance_2` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_executeQuery"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">executeQuery</text><text x="694.0" y="65" class="duplicate-count"> (2)</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `balance_2`

**데이터 흐름:**
```
EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.executeQuery -> EventControl.DatabaseExample.println
```

## 흐름 13: `balance` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_getDouble"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getDouble</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `balance`

**데이터 흐름:**
```
EventControl.DatabaseExample.getDouble -> EventControl.DatabaseExample.println
```

## 흐름 14: `balance_1` - 상

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_getDouble"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getDouble</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `balance_1`

**데이터 흐름:**
```
EventControl.DatabaseExample.getDouble -> EventControl.DatabaseExample.println
```

## 흐름 15: `line` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="465.0" y="10" width="270" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SocketClient</text><g id="EventControl_SocketClient_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text></g><g id="EventControl_SocketClient_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `line`

**데이터 흐름:**
```
EventControl.SocketClient.nextLine -> EventControl.SocketClient.println
```

## 흐름 16: `line_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="465.0" y="10" width="270" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SocketClient</text><g id="EventControl_SocketClient_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text></g><g id="EventControl_SocketClient_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `line_1`

**데이터 흐름:**
```
EventControl.SocketClient.nextLine -> EventControl.SocketClient.println
```

## 흐름 17: `name` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="460.0" y="10" width="280" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SwitchExample</text><g id="EventControl_SwitchExample_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text></g><g id="EventControl_SwitchExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name`

**데이터 흐름:**
```
EventControl.SwitchExample.nextLine -> EventControl.SwitchExample.println
```

## 흐름 18: `name_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="460.0" y="10" width="280" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SwitchExample</text><g id="EventControl_SwitchExample_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text></g><g id="EventControl_SwitchExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name_1`

**데이터 흐름:**
```
EventControl.SwitchExample.nextLine -> EventControl.SwitchExample.println
```

## 흐름 19: `age` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="460.0" y="10" width="280" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SwitchExample</text><g id="EventControl_SwitchExample_nextInt"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextInt</text></g><g id="EventControl_SwitchExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `age`

**데이터 흐름:**
```
EventControl.SwitchExample.nextInt -> EventControl.SwitchExample.println
```

## 흐름 20: `age_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="460.0" y="10" width="280" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.SwitchExample</text><g id="EventControl_SwitchExample_nextInt"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextInt</text></g><g id="EventControl_SwitchExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `age_1`

**데이터 흐름:**
```
EventControl.SwitchExample.nextInt -> EventControl.SwitchExample.println
```

## 흐름 21: `id` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_getInt"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getInt</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `id`

**데이터 흐름:**
```
EventControl.DatabaseExample.getInt -> EventControl.DatabaseExample.println
```

## 흐름 22: `id_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_getInt"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getInt</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `id_1`

**데이터 흐름:**
```
EventControl.DatabaseExample.getInt -> EventControl.DatabaseExample.println
```

## 흐름 23: `name` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_getString"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getString</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name`

**데이터 흐름:**
```
EventControl.DatabaseExample.getString -> EventControl.DatabaseExample.println
```

## 흐름 24: `name_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="450.0" y="10" width="300" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.DatabaseExample</text><g id="EventControl_DatabaseExample_getString"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">getString</text></g><g id="EventControl_DatabaseExample_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `name_1`

**데이터 흐름:**
```
EventControl.DatabaseExample.getString -> EventControl.DatabaseExample.println
```

## 흐름 25: `date` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="480.0" y="10" width="240" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.inputDate</text><g id="EventControl_inputDate_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text></g><g id="EventControl_inputDate_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `date`

**데이터 흐름:**
```
EventControl.inputDate.readLine -> EventControl.inputDate.println
```

## 흐름 26: `date_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="480.0" y="10" width="240" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.inputDate</text><g id="EventControl_inputDate_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text></g><g id="EventControl_inputDate_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `date_1`

**데이터 흐름:**
```
EventControl.inputDate.readLine -> EventControl.inputDate.println
```

## 흐름 6: `leftMenus` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="0.0" y="10" width="240" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="120.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl.inputMenu</text><g id="EventControl_inputMenu_readLine"><circle cx="120.0" cy="60" r="5" class="node" /><text x="130.0" y="65" class="node-text">readLine</text></g><rect x="290.0" y="10" width="140" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="360.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControl</text><g id="EventControl_catchMenuError"><circle cx="360.0" cy="60" r="5" class="node" /><text x="370.0" y="65" class="node-text">catchMenuError</text></g><rect x="505.0" y="10" width="190" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">EventControlError</text><g id="EventControlError_checkMenuError"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">checkMenuError</text></g><g id="EventControlError_checkOneMenuErrors"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">checkOneMenuErrors</text><text x="736.0" y="115" class="duplicate-count"> (2)</text></g><rect x="780.0" y="10" width="120" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="840.0" y="30" class="class-text" text-anchor="middle" fill="white">EventModel</text><g id="EventModel_setOrderedMenu"><circle cx="840.0" cy="60" r="5" class="node" /><text x="850.0" y="65" class="node-text">setOrderedMenu</text><text x="948.0" y="65" class="duplicate-count"> (2)</text></g><rect x="945.0" y="10" width="270" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1080.0" y="30" class="class-text" text-anchor="middle" fill="white">EventModel.setOrderedMenu</text><g id="EventModel_setOrderedMenu_println"><circle cx="1080.0" cy="60" r="5" class="node" /><text x="1090.0" y="65" class="node-text">println</text></g><path d="M120.0,60 C180.0,108.0 300.0,108.0 360.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M360.0,60 C420.0,108.0 540.0,108.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,110 C660.0,154.03060268852505 780.0,114.03060268852505 840.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M840.0,60 C900.0,108.0 1020.0,108.0 1080.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `leftMenus`

**데이터 흐름:**
```
EventControl.inputMenu.readLine -> EventControl.catchMenuError -> EventControlError.checkMenuError -> EventControlError.checkOneMenuErrors -> EventControlError.checkOneMenuErrors -> EventModel.setOrderedMenu -> EventModel.setOrderedMenu -> EventModel.setOrderedMenu.println
```

## 흐름 28: `parsedDate` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="505.0" y="10" width="190" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.inputDate</text><g id="Example_inputDate_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="Example_inputDate_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `parsedDate`

**데이터 흐름:**
```
Example.inputDate.readLine -> Example.inputDate.readLine -> Example.inputDate.println
```

## 흐름 29: `parsedDate_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="505.0" y="10" width="190" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.inputDate</text><g id="Example_inputDate_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="Example_inputDate_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `parsedDate_1`

**데이터 흐름:**
```
Example.inputDate.readLine -> Example.inputDate.readLine -> Example.inputDate.println
```

## 흐름 30: `parsedDate_2` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="505.0" y="10" width="190" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.inputDate</text><g id="Example_inputDate_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="Example_inputDate_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `parsedDate_2`

**데이터 흐름:**
```
Example.inputDate.readLine -> Example.inputDate.readLine -> Example.inputDate.println
```

## 흐름 31: `menu` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="505.0" y="10" width="190" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.inputMenu</text><g id="Example_inputMenu_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text></g><g id="Example_inputMenu_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `menu`

**데이터 흐름:**
```
Example.inputMenu.readLine -> Example.inputMenu.println
```

## 흐름 32: `menu_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="505.0" y="10" width="190" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.inputMenu</text><g id="Example_inputMenu_readLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">readLine</text></g><g id="Example_inputMenu_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `menu_1`

**데이터 흐름:**
```
Example.inputMenu.readLine -> Example.inputMenu.println
```

## 흐름 33: `part` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="45.0" y="10" width="310" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="200.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.processMultipleInputs</text><g id="Example_processMultipleInputs_readLine"><circle cx="200.0" cy="60" r="5" class="node" /><text x="210.0" y="65" class="node-text">readLine</text><text x="266.0" y="65" class="duplicate-count"> (3)</text></g><rect x="555.0" y="10" width="90" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example</text><g id="Example_handleInputPart"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">handleInputPart</text></g><rect x="875.0" y="10" width="250" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1000.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.handleInputPart</text><g id="Example_handleInputPart_println"><circle cx="1000.0" cy="60" r="5" class="node" /><text x="1010.0" y="65" class="node-text">println</text></g><path d="M200.0,60 C300.0,140.0 500.0,140.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C700.0,140.0 900.0,140.0 1000.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `part`

**데이터 흐름:**
```
Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.handleInputPart -> Example.handleInputPart.println
```

## 흐름 34: `part_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="45.0" y="10" width="310" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="200.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.processMultipleInputs</text><g id="Example_processMultipleInputs_readLine"><circle cx="200.0" cy="60" r="5" class="node" /><text x="210.0" y="65" class="node-text">readLine</text><text x="266.0" y="65" class="duplicate-count"> (3)</text></g><rect x="555.0" y="10" width="90" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example</text><g id="Example_handleInputPart"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">handleInputPart</text></g><rect x="875.0" y="10" width="250" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1000.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.handleInputPart</text><g id="Example_handleInputPart_println"><circle cx="1000.0" cy="60" r="5" class="node" /><text x="1010.0" y="65" class="node-text">println</text></g><path d="M200.0,60 C300.0,140.0 500.0,140.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C700.0,140.0 900.0,140.0 1000.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `part_1`

**데이터 흐름:**
```
Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.handleInputPart -> Example.handleInputPart.println
```

## 흐름 35: `part_2` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="45.0" y="10" width="310" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="200.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.processMultipleInputs</text><g id="Example_processMultipleInputs_readLine"><circle cx="200.0" cy="60" r="5" class="node" /><text x="210.0" y="65" class="node-text">readLine</text><text x="266.0" y="65" class="duplicate-count"> (3)</text></g><rect x="555.0" y="10" width="90" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example</text><g id="Example_handleInputPart"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">handleInputPart</text></g><rect x="875.0" y="10" width="250" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1000.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.handleInputPart</text><g id="Example_handleInputPart_println"><circle cx="1000.0" cy="60" r="5" class="node" /><text x="1010.0" y="65" class="node-text">println</text></g><path d="M200.0,60 C300.0,140.0 500.0,140.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C700.0,140.0 900.0,140.0 1000.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `part_2`

**데이터 흐름:**
```
Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.handleInputPart -> Example.handleInputPart.println
```

## 흐름 36: `part_3` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="45.0" y="10" width="310" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="200.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.processMultipleInputs</text><g id="Example_processMultipleInputs_readLine"><circle cx="200.0" cy="60" r="5" class="node" /><text x="210.0" y="65" class="node-text">readLine</text><text x="266.0" y="65" class="duplicate-count"> (3)</text></g><rect x="555.0" y="10" width="90" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example</text><g id="Example_handleInputPart"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">handleInputPart</text></g><rect x="875.0" y="10" width="250" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1000.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.handleInputPart</text><g id="Example_handleInputPart_println"><circle cx="1000.0" cy="60" r="5" class="node" /><text x="1010.0" y="65" class="node-text">println</text></g><path d="M200.0,60 C300.0,140.0 500.0,140.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C700.0,140.0 900.0,140.0 1000.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `part_3`

**데이터 흐름:**
```
Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.handleInputPart -> Example.handleInputPart.println
```

## 흐름 37: `part_4` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="45.0" y="10" width="310" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="200.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.processMultipleInputs</text><g id="Example_processMultipleInputs_readLine"><circle cx="200.0" cy="60" r="5" class="node" /><text x="210.0" y="65" class="node-text">readLine</text><text x="266.0" y="65" class="duplicate-count"> (3)</text></g><rect x="555.0" y="10" width="90" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example</text><g id="Example_handleInputPart"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">handleInputPart</text></g><rect x="875.0" y="10" width="250" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1000.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.handleInputPart</text><g id="Example_handleInputPart_println"><circle cx="1000.0" cy="60" r="5" class="node" /><text x="1010.0" y="65" class="node-text">println</text></g><path d="M200.0,60 C300.0,140.0 500.0,140.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C700.0,140.0 900.0,140.0 1000.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `part_4`

**데이터 흐름:**
```
Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.handleInputPart -> Example.handleInputPart.println
```

## 흐름 38: `part_5` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="45.0" y="10" width="310" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="200.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.processMultipleInputs</text><g id="Example_processMultipleInputs_readLine"><circle cx="200.0" cy="60" r="5" class="node" /><text x="210.0" y="65" class="node-text">readLine</text><text x="266.0" y="65" class="duplicate-count"> (3)</text></g><rect x="555.0" y="10" width="90" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">Example</text><g id="Example_handleInputPart"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">handleInputPart</text></g><rect x="875.0" y="10" width="250" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="1000.0" y="30" class="class-text" text-anchor="middle" fill="white">Example.handleInputPart</text><g id="Example_handleInputPart_println"><circle cx="1000.0" cy="60" r="5" class="node" /><text x="1010.0" y="65" class="node-text">println</text></g><path d="M200.0,60 C300.0,140.0 500.0,140.0 600.0,60" class="edge" marker-end="url(#arrowhead)" /><path d="M600.0,60 C700.0,140.0 900.0,140.0 1000.0,60" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `part_5`

**데이터 흐름:**
```
Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.processMultipleInputs.readLine -> Example.handleInputPart -> Example.handleInputPart.println
```

## 흐름 39: `result` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="495.0" y="10" width="210" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">InputProcessor.main</text><g id="InputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="InputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `result`

**데이터 흐름:**
```
InputProcessor.main.nextLine -> InputProcessor.main.nextLine -> InputProcessor.main.println
```

## 흐름 40: `result_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="495.0" y="10" width="210" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">InputProcessor.main</text><g id="InputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="InputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `result_1`

**데이터 흐름:**
```
InputProcessor.main.nextLine -> InputProcessor.main.nextLine -> InputProcessor.main.println
```

## 흐름 41: `result_2` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="495.0" y="10" width="210" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">InputProcessor.main</text><g id="InputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="InputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `result_2`

**데이터 흐름:**
```
InputProcessor.main.nextLine -> InputProcessor.main.nextLine -> InputProcessor.main.println
```

## 흐름 42: `result_3` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="495.0" y="10" width="210" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">InputProcessor.main</text><g id="InputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="InputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `result_3`

**데이터 흐름:**
```
InputProcessor.main.nextLine -> InputProcessor.main.nextLine -> InputProcessor.main.println
```

## 흐름 43: `finalOutput` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="490.0" y="10" width="220" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">OutputProcessor.main</text><g id="OutputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="OutputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `finalOutput`

**데이터 흐름:**
```
OutputProcessor.main.nextLine -> OutputProcessor.main.nextLine -> OutputProcessor.main.println
```

## 흐름 44: `finalOutput_1` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="490.0" y="10" width="220" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">OutputProcessor.main</text><g id="OutputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="OutputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `finalOutput_1`

**데이터 흐름:**
```
OutputProcessor.main.nextLine -> OutputProcessor.main.nextLine -> OutputProcessor.main.println
```

## 흐름 45: `finalOutput_2` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="490.0" y="10" width="220" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">OutputProcessor.main</text><g id="OutputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="OutputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `finalOutput_2`

**데이터 흐름:**
```
OutputProcessor.main.nextLine -> OutputProcessor.main.nextLine -> OutputProcessor.main.println
```

## 흐름 46: `finalOutput_3` - 중

<div class='call-graph'>
<?xml version="1.0" encoding="UTF-8"?>
        <svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
            <style>
                .node { fill: blue; }
                .node-text { font-size: 12px; }
                .class-label { fill: white; }
                .class-text { font-size: 14px; font-weight: bold; }
                .edge { stroke: black; fill: none; stroke-width: 1.5; }
                .background { fill: white; }
                .duplicate-count { font-size: 10px; fill: red; font-weight: bold; }
            </style>
            <rect width="100%" height="100%" class="background"/>
        <rect x="490.0" y="10" width="220" height="30" rx="5" ry="5" fill="#4a4a4a"/><text x="600.0" y="30" class="class-text" text-anchor="middle" fill="white">OutputProcessor.main</text><g id="OutputProcessor_main_nextLine"><circle cx="600.0" cy="60" r="5" class="node" /><text x="610.0" y="65" class="node-text">nextLine</text><text x="666.0" y="65" class="duplicate-count"> (2)</text></g><g id="OutputProcessor_main_println"><circle cx="600.0" cy="110" r="5" class="node" /><text x="610.0" y="115" class="node-text">println</text></g><path d="M600.0,60 C600.0,45.0 600.0,85.0 600.0,110" class="edge" marker-end="url(#arrowhead)" />
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="black" />
                </marker>
            </defs>
        </svg></div>

**오염된 변수:** `finalOutput_3`

**데이터 흐름:**
```
OutputProcessor.main.nextLine -> OutputProcessor.main.nextLine -> OutputProcessor.main.println
```

<style>
.call-graph { overflow: auto; max-width: 100%; max-height: 600px; border: 1px solid #ddd; margin-bottom: 20px; }
.call-graph svg { min-width: 100%; min-height: 100%; }
</style>
