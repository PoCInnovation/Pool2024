# Setup - Svelte setup

Today we will need to use a lot of new tools. Don't worry if you don't know them, you will guide to use them.

First, we will need to install `nvm`. `nvm` is a node version manager, it will allow us to install multiple versions of `nodejs` and switch between them easily. `Nodejs` is a javascript runtime, it will allow us to run javascript outside of the browser. Click [here](https://github.com/nvm-sh/nvm#installing-and-updating) to install `nvm`.

Then, we will need to install `npm`. `npm` is a package manager, it will allow us to install packages. Normally, `npm` is installed with `nvm`. If it is not the case, click [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) to install `npm`.

Now, we will install `Svelte`. `Svelte` is a javascript framework. It will allow us to create a web application, quickly and easily. To install `Svelte`, run the following command in your terminal.

```bash
npm create svelte@latest if_you_copy_paste_this_you_are_a_sheep
```

Enter `y` to install `create svelte` package. Then, select `Skeleton project`, `Yes, using TypeScript syntax` and `Add ESLint for code linting`.

Run your app to check if everything is working fine:

```bash
cd if_you_copy_paste_this_you_are_a_sheep
npm install
npm run dev
```

Open your browser and go to `http://localhost:5173`. You should see a `Hello world!` message.

Finally, we will install `Viem`. `Viem` is a typescript interface for ethereum. It will allow us to interact with the blockchain. To install `Viem`, run the following command in your terminal.

```bash
npm install viem
```

## Back to the workshop

[Jump !](./README.md)
