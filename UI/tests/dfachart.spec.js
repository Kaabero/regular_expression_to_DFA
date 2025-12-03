// @ts-check
import { test, expect} from '@playwright/test'
import { describe } from 'node:test'



describe('DfaChart', () => {
  
  test('after valid input dfachart is renered after pressing button Näytä kuva', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('(a|b)*abb')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await expect(page.getByText('Säännöllisen lausekkeen "(a|b)*abb" DFA:')).toBeVisible()
    await page.getByRole('button', { name: 'Näytä kuva' }).click()
    await expect(page.getByRole('button', { name: 'Aloita alusta' })).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä tiedot' })).toBeVisible()
    await expect(page.getByRole('button', { name: 'Näytä kuva' })).not.toBeVisible()
    await page.waitForSelector('.react-flow__pane')
    const edge = page.locator('.react-flow__edge-path')
    const node = page.locator('.react-flow__node')
    
    await expect(edge).toHaveCount(8)
    await expect(node).toHaveCount(4)

  })

  test('dfachart with selfconnecting edge is rendered with edge label', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('a*')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await page.getByRole('button', { name: 'Näytä kuva' }).click()
    await page.waitForSelector('.react-flow__pane')
    const edge = page.locator('.react-flow__edge-path')
    const node =page.locator('.react-flow__node')
    await expect(edge).toHaveCount(1)
    await expect(node).toHaveCount(1)
    await expect(page.locator('.edge')).toHaveText('a')

  })

  test('dfachart with overlapping edges is rendered with all edge labels', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('(ab)*')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await page.getByRole('button', { name: 'Näytä kuva' }).click()
    await page.waitForSelector('.react-flow__pane')
    const edge = page.locator('.react-flow__edge-path')
    const node =page.locator('.react-flow__node')
    await expect(edge).toHaveCount(6)
    await expect(node).toHaveCount(3)
    const chart = page.locator('.react-flow')
    await expect(chart).toContainText('a, b')

  })

  test('dfachart with bidirectional edges is rendered with both edge labels', async ({page}) => {
    await page.goto('http://localhost:5173')
    await page.getByRole('textbox').fill('(aa)*')
    await page.getByRole('button', { name: 'Luo DFA' }).click()
    await page.getByRole('button', { name: 'Näytä kuva' }).click()
    await page.waitForSelector('.react-flow__pane')
    const edge = page.locator('.react-flow__edge-path')
    const node =page.locator('.react-flow__node')
    await expect(edge).toHaveCount(2)
    await expect(node).toHaveCount(2)
    const chart = page.locator('.react-flow')
    const count = await chart.getByText('a', { exact: true }).count()
    expect(count).toBe(2)

  })
})
