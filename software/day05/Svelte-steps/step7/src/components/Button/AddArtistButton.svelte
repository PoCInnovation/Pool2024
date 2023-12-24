<script lang="ts">
    import { Button } from "flowbite-svelte";
    import AddArtistModal from "../AddArtistModal.svelte";
    import type { Artist } from "../../types/Artist.svelte";

    export let artists:Artist[];
    let openModal = false;
</script>

<Button on:click={() => openModal = !openModal}>Add an artist</Button>
<AddArtistModal openModal={openModal} artists={artists}/>