# Arquitetura de Software

A base de todas essas arquiteturas é o **Desacoplamento**. Quanto menos uma parte do código souber sobre a outra, mais fácil será trocar as peças. No MVC, separamos o "como mostrar" do "o que mostrar". Na Clean Architecture, levamos isso ao extremo, isolando a regra de negócio (o "porquê" do software existir) de qualquer tecnologia externa.

---

### 1. View (e Modularização)

Foca na quebra da interface em blocos independentes. Cada módulo é um "pacote" completo que resolve um problema visual ou funcional, facilitando o reuso e a manutenção isolada sem afetar o restante da aplicação.

**Estrutura de Pastas:**

```text
src/
  components/
    Button/
    Navbar/
  modules/
    Login/
    Dashboard/
  shared/
    hooks/
    utils/

```

**Como Arquitetar:**
Você deve pensar no sistema como um Lego. Elementos básicos ficam em `components`. Telas ou fluxos completos ficam em `modules`. O segredo é evitar que um módulo dependa diretamente de outro módulo; eles devem se comunicar apenas através de estados globais ou rotas.

---

### 2. Document-View

Separa os dados brutos e sua lógica de processamento (**Document**) da forma como esses dados são apresentados (**View**). É a arquitetura ideal para sistemas que precisam de múltiplas visualizações simultâneas para o mesmo dado.

**Estrutura de Pastas:**

```text
src/
  document/
    TextProcessor/
    FileBuffer/
  view/
    MainEditor/
    PrintPreview/

```

**Como Arquitetar:**
O `Document` é o coração. Ele gerencia a leitura e escrita de arquivos ou memória. A `View` apenas "assiste" ao documento. Se você mudar um parágrafo no documento, todas as visualizações (Editor e Pré-visualização) mudam automaticamente.

---

### 3. MVC (Model-View-Controller)

Divide a aplicação em três camadas: o **Model** (dados e regras), a **View** (interface) e o **Controller** (o mediador). O Controller recebe o comando, manipula o Model e decide qual View será exibida.

**Estrutura de Pastas:**

```text
src/
  controllers/
    UserController/
  models/
    User/
  views/
    UserRegistration/

```

**Como Arquitetar:**
O fluxo é unidirecional: Usuário -> Controller -> Model -> View. O Model nunca deve saber que o Controller existe. Isso permite que você teste a lógica de salvar um usuário (Model) sem nem precisar abrir o navegador ou a interface.

---

### 4. Clean Architecture

Organiza o software em camadas concêntricas. O centro contém as **Entidades** e **Casos de Uso** (regras de negócio). As camadas externas contêm detalhes técnicos como bancos de dados, frameworks e interfaces de usuário.

**Estrutura de Pastas:**

```text
src/
  core/
    entities/
    usecases/
  adapters/
    controllers/
    repositories/
  infrastructure/
    database/
    http/

```

**Como Arquitetar:**
A regra absoluta é: as dependências apontam para dentro. O banco de dados depende da regra de negócio, mas a regra de negócio jamais depende do banco. Isso é feito através de interfaces (contratos) definidos no centro e implementados fora.

---
---

