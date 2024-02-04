# PoC P2P Pool 2024 - Day 04 - Decentralized App

**Day purposes**

✔ Build a decentralized application with Svelte

✔ Interact with your ERC-721 smart contract

✔ Learn about Viem

## Introduction

Decentralized applications are applications that interact with the blockchain. For example when you want to swap some tokens on uniswap, you are using a decentralized application. The goal of this day is to create your own decentralized application that will interact with your ERC-721 smart contract.

## Step 0 - Setup

Please refer to [SETUP.md](SETUP.md) file. It is not the same as the previous day.

## Step 1 - Connecting your wallet to your web application

### 📑 **Description**:

The goal of this task is to connnect your wallet to your web application and be able to get its balance and display it to the user. You will use the `viem` library to do so. `Viem` is a typescript interface for ethereum. It will allow us to interact with the blockchain. For this step, you will need to have a wallet with some testnet ether on it. You can use [metamask](https://metamask.io/) and [sepolia faucet](https://sepoliafaucet.com/) for example.

### 📌 **Tasks**:

In the `src/routes/+page.svelte` file:

- Create a button that will ask you to connect your wallet to the website
- Display your account's address
- Display your account's balance
  > 💡 Use `sepolia` instead of `mainet`

### 📚 **Documentation**:

Take a look at [Svelte examples](https://svelte.dev/examples/hello-world).
Check out the [documentation](https://viem.sh/docs/getting-started.html) of viem and their [examples](https://github.com/wevm/viem/tree/main/examples) to connect your wallet.

### ✔️ **Validation**:

You can now ask to the user to connect their wallet and display information about it on the page !

## Step 2 - Calling your smart contract's functions from your application

### 📑 **Description**:

During this step, you will use your ERC-721 smart contract that you created in the day02. If you didn't do the day 2, please do it before or take the [openzeppellin implementation](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol).

Your goal now is to call your smart contract's function from your web application in order to interact with it.
The first one we are going to call is the `mint` function, which will let us create our NFT on the blockchain. To call this function, we need the address of your deployed contract and the "function prototypes" of your contract which is called `abi`.

### 📌 **Tasks**:

- Take the `CONTRACT_ADDRESS` of your ERC-721 contract that you have deployed. You will need it for the last task.
- In the `out` folder of the day2, take the `PetNFT.json` which is in the `PetNFT.sol` folder. Put it in the `src` folder of your Svelte application. You will need it for the last task.
- Now, create a button which will call the `mint` method of your ERC-721 contract.

### 📚 **Documentation**:

Take a look at [this](https://viem.sh/docs/contract/getContract.html), it will help you 😉.

### ✔️ **Validation**:

You minted your first NFT and can now see it in your collection in your [opensea testnet](https://testnets.opensea.io/account) account.

## Step 3 - Let's see our NFTs

### 📑 **Description**:

Minting NFTs is fun, but we want to see them now right ? Let's do it !

### 📌 **Tasks**:

- Create a new `/collection` page
- Create a `getAllNFTs()` function in your smart contract to retrieve all NFTs
- Call this function in your application and display them on the page

  > 💡 For this function, you will need to import some `abi` from day2. You can find them in the `out`. I let you find which one you need 😉

  > 💡 To get NFT information, you will need to call the `tokenURI` function of your ERC-721 contract.

### 📚 **Documentation**:

Check out the [sveltkit docs](https://kit.svelte.dev/docs/routing) to learn more about routing.

### ✔️ **Validation**:

You can now see all your NFTs on a new `/collection` page.

## Step 4 - Transferring NFTs

### 📑 **Description**:

Let's send an NFT to your friends !

### 📌 **Tasks**:

- When clicking on an NFT, show an input to the user to type in the address of the wallet you want to transfer the NFT to, and by pressing on a button, be able to transfer it.

### 📚 **Documentation**:

Check out the [ERC721 OpenZeppelin doc](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721) and find the transfer function.

### ✔️ **Validation**:

You can now send an NFT to another address ! Well done !!

## Bonus - Styling

Your application might not look really good. Use some styles to make it beautiful !
If you don't use tailwind, I will look for you, I will find you, and ... I will kill you !

## Conclusion

Well done ! You've accomplished a lot today, and there is so much more to discover.
Refer to the official documentations to deep-dive into these technologies :

- [Svelte](https://svelte.dev/docs/)
- [Viem](https://viem.sh/docs/getting-started.html)
- [Solidity](https://docs.soliditylang.org/en/v0.8.23/) (you should despise this website as it is made with chakra UI and we all know chakra UI is dog poop)

Hope you enjoyed this day !

## Authors

| [<img src="https://github.com/letamanoir.png?size=85" width=85><br><sub>Martin Saldinger</sub>](https://github.com/letamanoir) | [<img src="https://github.com/alexandregrare.png?size=85" width=85><br><sub>Alexandre Grare</sub>](https://github.com/alexandregrare) | [<img src="https://github.com/Toumi-Elyes.png?size=85" width=85><br><sub>Elyes Toumi</sub>](https://github.com/Toumi-Elyes) | [<img src="https://github.com/tonida-rodda.png?size=85" width=85><br><sub>Toni Da-Rodda</sub>](https://github.com/tonida-rodda) |
| :----------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------: |

<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white">
    </a>
</p>

> 🚀 Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.
