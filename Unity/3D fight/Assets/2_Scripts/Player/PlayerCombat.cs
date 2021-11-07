using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCombat : MonoBehaviour
{
    public float hp;
    [ReadOnly] public Weapon curWeapon;
    [HideInInspector] public Player player;
    public float attackComboLimitTime = 2f;

    private void Reset()
    {
        curWeapon = GetComponentInChildren<Weapon>();
        player = GetComponent<Player>();
        curWeapon.owner = player;
    }

    private void Awake()
    {
        curWeapon = GetComponentInChildren<Weapon>();
        player = GetComponent<Player>();
        curWeapon.owner = player;
    }


    public void Attack()
    {
        player._animator.Attack();
    }

    public void Damaged(Damaged damage)
    {
        Debug.Log($"{damage.attacker.name}가 {damage.attackPower}의 데미지를 입혔음");
    }

    public void CanDamagedTarget()
    {
        curWeapon.Enable(true);
    }

    public void CantDamagedTarget()
    {
        curWeapon.Enable(false);
    }
}
