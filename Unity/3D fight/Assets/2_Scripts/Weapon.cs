using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum AttackCheckMode
{
    Enable,
    Overlap
}

[RequireComponent(typeof(BoxCollider))]
public class Weapon : MonoBehaviour
{
    public AttackCheckMode checkMode = AttackCheckMode.Enable;
    // 콜라이더 활성 비활성화로 공격판정할 떄 쓰임
    [ReadOnly] public BoxCollider _col;
    [ReadOnly] public Player owner;
    public float attackPower;

    // OverlapBox로 공격판정할 때 쓰임
    public Vector3 center;

    private void OnDrawGizmos()
    {
        if (_col == null)
            _col = GetComponent<BoxCollider>();

        Gizmos.color = new Color(0.3f, 0.22f, 0.6f, 0.6f);
        Gizmos.matrix = Matrix4x4.TRS(transform.position, transform.rotation, transform.lossyScale);
        Gizmos.DrawCube(_col.center, Vector3.Scale(Vector3.one, _col.size));
    }

    private void Awake()
    {
        _col = GetComponent<BoxCollider>();
    }

    public void CheckAttackTarget()
    {

    }

    /// <summary>
    /// 특정 프레임 구간동안 트리거를 활성화 시켜주기 위한 방법
    /// </summary>
    /// <param name="isEnable"></param>
    public void Enable(bool isEnable)
    {
        _col.enabled = isEnable;
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            other.GetComponent<PlayerCombat>().Damaged(new Damaged(attackPower, owner));
        }
    }
}


public class Damaged
{
    public Player attacker;
    public float attackPower;

    public Damaged(float attackPower, Player attacker)
    {
        this.attackPower = attackPower;
        this.attacker = attacker;
    }
}