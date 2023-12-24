<script>
    import { push } from "svelte-spa-router";
    import { Heading, P, A, Mark, Secondary, Button } from 'flowbite-svelte';

    const goToLogin = () => {
        push("/login");
    }

    const goToRegister = () => {
        push("/register");
    }
</script>

<div class="flex flex-col text-center">
    <Heading tag="h1" class="text-center">Artists Book</Heading>
    <br/>
    <p class="text-lg text-center">Manage your favorite artists</p>
    <br/>
</div>
<div class="text-center">
    <Button on:click={goToLogin}>Login</Button>
    <Button on:click={goToRegister}>Register</Button>
</div>