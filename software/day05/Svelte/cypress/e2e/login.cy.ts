describe('Good front for Login page', () => {
	it('Go to login page', () => {
		cy.visit('/login');
	});

	beforeEach(() => {
		cy.visit('/login');
	});

	it('Good number of buttons', () => {
		cy.get('button').should('have.length', 2);
	});

	it('Good number of inputs', () => {
		cy.get('input').should('have.length', 2);
	});

	it('Good name for login button', () => {
		cy.get('#loginPage-login-button').should('contain', 'Login');
	});

	it('Good name for register button', () => {
		cy.get('#loginPage-register-button').should('contain', 'New user ? Register');
	});
});

describe('Register button in Login page', () => {
	it('Go to login page', () => {
		cy.visit('/login');
	});

	beforeEach(() => {
		cy.visit('/login');
	});

	it('Good URL redirect for register button', () => {
		cy.get('#loginPage-register-button').click().url().should('eq', `${Cypress.config().baseUrl}/register`);
	});
});
