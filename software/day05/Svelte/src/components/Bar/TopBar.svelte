<script lang="ts">
    import { Navbar, NavUl, Button, A } from "flowbite-svelte";
    import AddArtistButton from "../Button/AddArtistButton.svelte";
    import type { Artist } from "../../types/Artist.svelte";

    export let artists:Artist[];
</script>

<Navbar>
    <A href="/#/dashboard">Dashboard</A>
    <NavUl>
        <AddArtistButton artists={artists}/>
    </NavUl>
</Navbar>